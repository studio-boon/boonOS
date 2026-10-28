#!/usr/bin/env python3
"""Read-only, single-currency managerial ledger. Python standard library only."""

import argparse
from collections import defaultdict
from datetime import date
from decimal import Decimal, localcontext
import json
from pathlib import Path
import re
import sys


class LedgerError(ValueError):
    """An invalid input must never become a plausible financial report."""


ZERO = Decimal("0.00")
MONEY = re.compile(r"-?(?:0|[1-9][0-9]{0,14})(?:\.[0-9]{1,2})?\Z")


def require(condition, message):
    if not condition:
        raise LedgerError(message)


def object_fields(value, required, optional, label):
    require(isinstance(value, dict), f"{label}: esperado objeto")
    missing = set(required) - value.keys()
    extra = value.keys() - set(required) - set(optional)
    require(not missing, f"{label}: campos ausentes: {', '.join(sorted(missing))}")
    require(not extra, f"{label}: campos desconhecidos: {', '.join(sorted(extra))}")


def nonempty(value, label):
    require(isinstance(value, str) and bool(value.strip()), f"{label}: texto vazio ou inválido")
    return value


def day(value, label):
    require(isinstance(value, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", value),
            f"{label}: usar AAAA-MM-DD")
    try:
        return date.fromisoformat(value)
    except ValueError as error:
        raise LedgerError(f"{label}: data inválida") from error


def money(value, label, positive=False):
    require(isinstance(value, str) and MONEY.fullmatch(value) is not None,
            f"{label}: usar string decimal, até 2 casas, sem vírgula/moeda")
    result = Decimal(value)
    require(not positive or result > 0, f"{label}: valor deve ser positivo")
    return result


def amount(value):
    return format(value, ".2f")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"JSON: chave duplicada: {key}")
        result[key] = value
    return result


def read_json(path):
    with Path(path).open(encoding="utf-8") as stream:
        return json.load(stream, object_pairs_hook=unique_object)


def validate(data):
    object_fields(data, {"schema_version", "currency", "opening_cash", "obligations", "events"},
                  {"description"}, "ledger")
    require(type(data["schema_version"]) is int and data["schema_version"] == 1,
            "ledger: schema_version deve ser 1")
    require(isinstance(data["currency"], str) and re.fullmatch(r"[A-Z]{3}", data["currency"]),
            "ledger: currency deve ter 3 letras maiúsculas")
    if "description" in data:
        nonempty(data["description"], "description")
    opening = data["opening_cash"]
    object_fields(opening, {"date", "amount", "source"}, set(), "opening_cash")
    start = day(opening["date"], "opening_cash.date")
    money(opening["amount"], "opening_cash.amount")
    nonempty(opening["source"], "opening_cash.source")
    require(isinstance(data["obligations"], list), "obligations: esperado array")
    require(isinstance(data["events"], list), "events: esperado array")
    obligations = {}
    for item in data["obligations"]:
        object_fields(item, {"id", "kind", "state", "issued_on", "due_on", "amount", "description", "source"},
                      {"project_id", "party_id", "committed_on", "cancelled_on"}, "obligation")
        key = nonempty(item["id"], "obligation.id")
        require(key not in obligations, f"obligation: ID duplicado: {key}")
        require(item["kind"] in ("receivable", "payable"), f"{key}: kind inválido")
        require(item["state"] in ("forecast", "committed"), f"{key}: state inválido")
        issued = day(item["issued_on"], f"{key}.issued_on")
        due = day(item["due_on"], f"{key}.due_on")
        require(due >= issued, f"{key}: vencimento anterior à emissão")
        money(item["amount"], f"{key}.amount", positive=True)
        for field in ("description", "source", "project_id", "party_id"):
            if field in item:
                nonempty(item[field], f"{key}.{field}")
        if item["state"] == "committed":
            require("committed_on" in item, f"{key}: committed_on obrigatório")
            committed = day(item["committed_on"], f"{key}.committed_on")
            require(committed >= issued, f"{key}: compromisso anterior à emissão")
        else:
            require("committed_on" not in item, f"{key}: previsão não tem committed_on")
        if "cancelled_on" in item:
            cancelled = day(item["cancelled_on"], f"{key}.cancelled_on")
            require(cancelled >= issued, f"{key}: cancelamento anterior à emissão")
            if item["state"] == "committed":
                require(cancelled >= committed, f"{key}: cancelamento anterior ao compromisso")
        obligations[key] = item

    events = {}
    for index, event in enumerate(data["events"]):
        object_fields(event, {"id", "obligation_id", "date", "kind", "amount", "source"},
                      {"reverses"}, "event")
        key = nonempty(event["id"], "event.id")
        require(key not in events, f"event: ID duplicado: {key}")
        nonempty(event["obligation_id"], f"{key}.obligation_id")
        require(event["obligation_id"] in obligations, f"{key}: obrigação desconhecida")
        item = obligations[event["obligation_id"]]
        when = day(event["date"], f"{key}.date")
        require(when >= start, f"{key}: evento anterior ao saldo inicial")
        require(item["state"] == "committed", f"{key}: previsão não pode ser liquidada")
        require(when >= day(item["committed_on"], "committed_on"), f"{key}: evento antes do compromisso")
        if "cancelled_on" in item:
            require(when <= day(item["cancelled_on"], "cancelled_on"), f"{key}: evento após cancelamento")
        require(event["kind"] in ("settlement", "reversal"), f"{key}: kind inválido")
        money(event["amount"], f"{key}.amount", positive=True)
        nonempty(event["source"], f"{key}.source")
        if event["kind"] == "reversal":
            require("reverses" in event, f"{key}: reverses obrigatório")
            nonempty(event["reverses"], f"{key}.reverses")
        else:
            require("reverses" not in event, f"{key}: liquidação não pode conter reverses")
        events[key] = (event, index)

    ordered = sorted(events.values(), key=lambda pair: (pair[0]["date"], pair[1]))
    settled = defaultdict(lambda: ZERO)
    reversed_amounts = defaultdict(lambda: ZERO)
    seen = {}
    for event, _ in ordered:
        key = event["id"]
        item = obligations[event["obligation_id"]]
        value = Decimal(event["amount"])
        if event["kind"] == "reversal":
            original = seen.get(event["reverses"])
            require(original is not None, f"{key}: estorno deve referenciar evento anterior")
            require(original["kind"] == "settlement", f"{key}: estornar apenas liquidação")
            require(original["obligation_id"] == event["obligation_id"], f"{key}: obrigação do estorno diverge")
            reversed_amounts[original["id"]] += value
            require(reversed_amounts[original["id"]] <= Decimal(original["amount"]), f"{key}: estorno excede liquidação")
            settled[item["id"]] -= value
        else:
            settled[item["id"]] += value
        require(ZERO <= settled[item["id"]] <= Decimal(item["amount"]), f"{key}: liquidação excede saldo da obrigação")
        seen[key] = event
    for item in obligations.values():
        if "cancelled_on" in item:
            require(settled[item["id"]] == ZERO,
                    f"{item['id']}: cancelar requer estorno de toda liquidação; não apagar caixa")
    return obligations, [event for event, _ in ordered]


def build_report(data, as_of):
    """Validate the complete ledger, then compute its state at an explicit date."""
    with localcontext() as context:
        context.prec = 40
        return _build_report(data, as_of)


def _build_report(data, as_of):
    cutoff = day(as_of, "as_of")
    obligations, events = validate(data)
    require(cutoff >= day(data["opening_cash"]["date"], "opening_cash.date"),
            "as_of: anterior ao saldo inicial")
    settled = defaultdict(lambda: ZERO)
    totals = {name: ZERO for name in (
        "cash_in", "cash_out", "received_net", "paid_net", "receivable_committed",
        "payable_committed", "receivable_forecast", "payable_forecast",
        "receivable_overdue", "payable_overdue")}
    included_events = []
    for event in events:
        if day(event["date"], "date") > cutoff:
            continue
        item = obligations[event["obligation_id"]]
        signed = Decimal(event["amount"]) * (1 if event["kind"] == "settlement" else -1)
        settled[item["id"]] += signed
        incoming = item["kind"] == "receivable"
        totals["received_net" if incoming else "paid_net"] += signed
        cash_delta = signed if incoming else -signed
        totals["cash_in" if cash_delta > 0 else "cash_out"] += abs(cash_delta)
        included_events.append(event["id"])

    rows = []
    for key, item in sorted(obligations.items()):
        if day(item["issued_on"], "issued_on") > cutoff:
            continue
        cancelled = "cancelled_on" in item and day(item["cancelled_on"], "cancelled_on") <= cutoff
        committed = item["state"] == "committed" and day(item["committed_on"], "committed_on") <= cutoff
        state = "committed" if committed else "forecast"
        face = Decimal(item["amount"])
        balance = ZERO if cancelled else face - settled[key]
        liquidation = "settled" if settled[key] == face else "partial" if settled[key] > 0 else "pending"
        timing = "not_applicable"
        if balance > 0 and committed:
            due = day(item["due_on"], "due_on")
            timing = "overdue" if due < cutoff else "due_today" if due == cutoff else "not_due"
        if not cancelled:
            totals[f"{item['kind']}_{state}"] += balance
            if timing == "overdue":
                totals[f"{item['kind']}_overdue"] += balance
        rows.append({
            "id": key, "kind": item["kind"], "state": state,
            "validity": "cancelled" if cancelled else "active",
            "liquidation": liquidation, "timing": timing,
            "face_amount": amount(face), "settled_net": amount(settled[key]),
            "outstanding": amount(balance), "due_on": item["due_on"],
            "project_id": item.get("project_id"), "party_id": item.get("party_id"),
            "source": item["source"],
        })
    opening = Decimal(data["opening_cash"]["amount"])
    totals["opening_cash"] = opening
    totals["cash_balance"] = opening + totals["cash_in"] - totals["cash_out"]
    totals["cash_after_all_commitments"] = totals["cash_balance"] + totals["receivable_committed"] - totals["payable_committed"]
    return {
        "schema_version": 1, "currency": data["currency"], "as_of": as_of,
        "opening_date": data["opening_cash"]["date"],
        "totals": {key: amount(value) for key, value in totals.items()},
        "obligations": rows, "included_event_ids": included_events,
        "limits": [
            "Visão gerencial dos registros fornecidos; não comprova saldo bancário nem escrituração.",
            "cash_after_all_commitments é cenário sem prazo, não caixa disponível nem previsão de probabilidade.",
            "Recebimentos e pagamentos são líquidos de estornos; cash_in e cash_out mostram movimentos brutos.",
        ],
    }


def reconcile(data, statement, as_of):
    """Explicit IDs confirm links; date/value candidates remain suggestions."""
    report = build_report(data, as_of)
    obligations, events = validate(data)
    object_fields(statement, {"schema_version", "currency", "transactions"}, set(), "statement")
    require(type(statement["schema_version"]) is int and statement["schema_version"] == 1,
            "statement: schema_version deve ser 1")
    require(statement["currency"] == data["currency"], "statement: moeda diferente")
    require(isinstance(statement["transactions"], list), "statement.transactions: esperado array")
    cutoff = day(as_of, "as_of")
    start = day(data["opening_cash"]["date"], "opening_cash.date")
    signatures = {}
    for event in events:
        direction = "in" if obligations[event["obligation_id"]]["kind"] == "receivable" else "out"
        if event["kind"] == "reversal":
            direction = "out" if direction == "in" else "in"
        signatures[event["id"]] = (event["date"], direction, Decimal(event["amount"]))
    rows = []
    ids = set()
    linked = set()
    all_linked = set()
    considered = []
    for transaction in statement["transactions"]:
        object_fields(transaction, {"id", "date", "direction", "amount", "source"}, {"event_id"}, "transaction")
        key = nonempty(transaction["id"], "transaction.id")
        require(key not in ids, f"statement: ID duplicado: {key}")
        ids.add(key)
        when = day(transaction["date"], f"{key}.date")
        require(when >= start, f"{key}: transação anterior ao saldo inicial")
        require(transaction["direction"] in ("in", "out"), f"{key}: direção inválida")
        value = money(transaction["amount"], f"{key}.amount", positive=True)
        nonempty(transaction["source"], f"{key}.source")
        if "event_id" in transaction:
            reference = nonempty(transaction["event_id"], f"{key}.event_id")
            require(reference in signatures, f"{key}: event_id desconhecido")
            require(reference not in all_linked, f"{key}: evento vinculado duas vezes")
            all_linked.add(reference)
        if when <= cutoff:
            considered.append((transaction, value))
    for transaction, value in considered:
        key = transaction["id"]
        signature = (transaction["date"], transaction["direction"], value)
        reference = transaction.get("event_id")
        if reference:
            matched = signatures[reference] == signature and reference in report["included_event_ids"]
            if matched:
                linked.add(reference)
            rows.append({"transaction_id": key, "status": "matched" if matched else "divergence", "event_id": reference})
        else:
            rows.append({"transaction_id": key, "status": "pending", "candidate_event_ids": []})
    for row, (transaction, value) in zip(rows, considered):
        if row["status"] == "pending":
            signature = (transaction["date"], transaction["direction"], value)
            candidates = [key for key, value_signature in signatures.items()
                          if value_signature == signature and key not in all_linked
                          and key in report["included_event_ids"]]
            row["candidate_event_ids"] = sorted(candidates)
            row["status"] = "candidate" if len(candidates) == 1 else "ambiguous" if candidates else "unmatched"
    return {
        "schema_version": 1, "currency": data["currency"], "as_of": as_of,
        "transactions": rows,
        "unmatched_event_ids": sorted(set(report["included_event_ids"]) - linked),
        "complete": all(row["status"] == "matched" for row in rows)
                    and set(report["included_event_ids"]) == linked,
        "limits": ["Correspondência exata de dados fornecidos; não autentica extrato.",
                   "Sugestões não alteram o livro. Tarifas, pagamentos agrupados e datas diferentes exigem revisão."],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path, help="JSON do livro gerencial")
    parser.add_argument("--as-of", required=True, help="Data de corte AAAA-MM-DD")
    parser.add_argument("--statement", type=Path, help="JSON de extrato para conciliação por ID e sugestões exatas")
    args = parser.parse_args(argv)
    try:
        data = read_json(args.ledger)
        result = reconcile(data, read_json(args.statement), args.as_of) if args.statement else build_report(data, args.as_of)
    except (LedgerError, OSError, UnicodeError, json.JSONDecodeError) as error:
        print(f"Erro financeiro: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
