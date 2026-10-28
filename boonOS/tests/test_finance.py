"""Fictional ledger lifecycle, invalid evidence, time cuts and reconciliation."""

import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("finance", ROOT / "scripts" / "finance.py")
finance = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(finance)
FIXTURE = ROOT / "06. GUIAS" / "03. EXEMPLOS" / "operacao.json"


class FinanceTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def report(self, when="2026-09-25"):
        return finance.build_report(self.data, when)

    def row(self, key, when="2026-09-25"):
        return next(row for row in self.report(when)["obligations"] if row["id"] == key)

    def invalid(self, fragment):
        with self.assertRaisesRegex(finance.LedgerError, fragment):
            self.report()

    def test_end_to_end_partial_reversals_cancelled_and_future(self):
        report = self.report()
        expected = {
            "opening_cash": "1000.00", "received_net": "1000.00", "paid_net": "300.00",
            "cash_balance": "1700.00", "cash_in": "1800.00", "cash_out": "1100.00",
            "receivable_committed": "1400.00", "payable_committed": "500.00",
            "receivable_forecast": "900.00", "payable_forecast": "200.00",
            "receivable_overdue": "1000.00", "payable_overdue": "400.00",
            "cash_after_all_commitments": "2600.00",
        }
        self.assertEqual(report["totals"], expected)
        self.assertEqual(self.row("R-001")["liquidation"], "partial")
        self.assertEqual(self.row("R-001")["timing"], "overdue")
        self.assertEqual(self.row("RC-001")["validity"], "cancelled")
        self.assertEqual(self.row("RC-001")["outstanding"], "0.00")
        self.assertNotIn("E-007", report["included_event_ids"])

    def test_cutoff_before_cancel_preserves_money_and_after_future_includes_it(self):
        row = self.row("RC-001", "2026-09-17")
        self.assertEqual((row["validity"], row["liquidation"]), ("active", "settled"))
        self.assertEqual(self.report("2026-09-17")["totals"]["cash_balance"], "2300.00")
        self.assertEqual(self.report("2026-10-01")["totals"]["cash_balance"], "2100.00")

    def test_liquidation_and_overdue_are_independent(self):
        self.assertEqual(self.row("R-001", "2026-09-20")["timing"], "due_today")
        self.assertEqual(self.row("R-001", "2026-09-19")["timing"], "not_due")
        self.assertEqual(self.row("PR-001", "2026-11-01")["timing"], "not_applicable")

    def test_commitment_date_preserves_forecast_history(self):
        self.data["obligations"][1]["committed_on"] = "2026-09-30"
        self.assertEqual(self.row("R-002")["state"], "forecast")
        self.assertEqual(self.report()["totals"]["receivable_committed"], "1000.00")
        self.assertEqual(self.report()["totals"]["receivable_forecast"], "1300.00")

    def test_duplicate_event_reimport_rejected(self):
        self.data["events"].append(copy.deepcopy(self.data["events"][0]))
        self.invalid("ID duplicado")

    def test_duplicate_obligation_rejected(self):
        self.data["obligations"].append(copy.deepcopy(self.data["obligations"][0]))
        self.invalid("ID duplicado")

    def test_overpayment_rejected_before_later_reversal_can_hide_it(self):
        self.data["events"][0]["amount"] = "2100.00"
        self.invalid("liquidação excede")

    def test_partial_reversal_cannot_be_replayed_beyond_original(self):
        self.data["events"].append({"id": "E-008", "obligation_id": "R-001", "date": "2026-09-24", "kind": "reversal", "amount": "1100.00", "reverses": "E-001", "source": "demo:excesso"})
        self.invalid("estorno excede")

    def test_reversal_wrong_obligation_and_reversal_of_reversal_rejected(self):
        self.data["events"][4]["reverses"] = "E-002"
        self.invalid("obrigação do estorno diverge")
        self.data["events"][4]["reverses"] = "E-004"
        self.invalid("estornar apenas liquidação")

    def test_reversal_before_original_rejected(self):
        self.data["events"][4]["date"] = "2026-09-11"
        self.invalid("evento anterior")

    def test_cancelled_obligation_cannot_hide_received_cash(self):
        self.data["events"] = [event for event in self.data["events"] if event["id"] != "E-004"]
        self.invalid("cancelar requer estorno")

    def test_payment_after_cancellation_rejected(self):
        self.data["events"][3]["date"] = "2026-09-20"
        self.invalid("evento após cancelamento")

    def test_forecast_cannot_be_paid(self):
        self.data["events"][0]["obligation_id"] = "PR-001"
        self.invalid("previsão não pode")

    def test_missing_value_is_unknown_not_zero(self):
        del self.data["obligations"][0]["amount"]
        self.invalid("campos ausentes")

    def test_unknown_fields_rejected_to_catch_schema_typos(self):
        self.data["events"][0]["paid"] = True
        self.invalid("campos desconhecidos")

    def test_non_decimal_and_invalid_amounts_rejected(self):
        for value in (1.2, None, "1,20", "NaN", "Infinity", "-1.00", "0.00", "1.234", "1e3"):
            with self.subTest(value=value):
                self.data["events"][0]["amount"] = value
                self.invalid("valor deve ser positivo|usar string decimal")

    def test_cent_precision_and_no_mutation(self):
        data = {"schema_version": 1, "currency": "BRL", "opening_cash": {"date": "2026-09-01", "amount": "0.00", "source": "demo:saldo"},
                "obligations": [{"id": "r", "kind": "receivable", "state": "committed", "issued_on": "2026-09-01", "committed_on": "2026-09-01", "due_on": "2026-09-25", "amount": "0.30", "description": "centavos", "source": "demo:centavos"}],
                "events": [{"id": f"e{i}", "obligation_id": "r", "date": "2026-09-20", "kind": "settlement", "amount": value, "source": f"demo:centavos:{i}"} for i, value in enumerate(("0.10", "0.20"))]}
        original = copy.deepcopy(data)
        self.assertEqual(finance.build_report(data, "2026-09-25")["totals"]["cash_balance"], "0.30")
        self.assertEqual(data, original)

    def test_invalid_dates_and_cutoff_rejected(self):
        self.data["events"][0]["date"] = "2026-02-30"
        self.invalid("data inválida")
        with self.assertRaisesRegex(finance.LedgerError, "usar AAAA-MM-DD"):
            finance.build_report(self.data, "25/09/2026")

    def test_duplicate_json_key_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"amount":"1.00","amount":"2.00"}', encoding="utf-8")
            with self.assertRaisesRegex(finance.LedgerError, "chave duplicada"):
                finance.read_json(path)

    def statement(self):
        transactions = []
        obligations = {item["id"]: item for item in self.data["obligations"]}
        for event in self.data["events"]:
            if event["date"] > "2026-09-25":
                continue
            incoming = obligations[event["obligation_id"]]["kind"] == "receivable"
            if event["kind"] == "reversal":
                incoming = not incoming
            transactions.append({"id": "bank-" + event["id"], "date": event["date"], "direction": "in" if incoming else "out", "amount": event["amount"], "source": "demo:extrato:" + event["id"], "event_id": event["id"]})
        return {"schema_version": 1, "currency": "BRL", "transactions": transactions}

    def test_exact_reconciliation_and_divergence(self):
        statement = self.statement()
        self.assertTrue(finance.reconcile(self.data, statement, "2026-09-25")["complete"])
        statement["transactions"][0]["amount"] = "1199.99"
        report = finance.reconcile(self.data, statement, "2026-09-25")
        self.assertFalse(report["complete"])
        self.assertEqual(report["transactions"][0]["status"], "divergence")

    def test_reconciliation_candidate_is_never_automatic_match(self):
        statement = self.statement()
        del statement["transactions"][0]["event_id"]
        report = finance.reconcile(self.data, statement, "2026-09-25")
        self.assertFalse(report["complete"])
        self.assertEqual(report["transactions"][0]["status"], "candidate")
        self.assertEqual(report["transactions"][0]["candidate_event_ids"], ["E-001"])

    def test_reconciliation_ambiguous_candidates_remain_pending(self):
        self.data["events"][0]["amount"] = "600.00"
        extra = copy.deepcopy(self.data["events"][0])
        extra["id"], extra["source"] = "E-008", "demo:outro-comprovante"
        self.data["events"].append(extra)
        statement = {"schema_version": 1, "currency": "BRL", "transactions": [{"id": "bank-1", "date": "2026-09-15", "direction": "in", "amount": "600.00", "source": "demo:extrato:1"}]}
        report = finance.reconcile(self.data, statement, "2026-09-25")
        self.assertEqual(report["transactions"][0]["status"], "ambiguous")

    def test_reconciliation_duplicate_reference_and_currency_rejected(self):
        statement = self.statement()
        duplicate = copy.deepcopy(statement["transactions"][0])
        duplicate["id"] = "bank-other"
        statement["transactions"].append(duplicate)
        with self.assertRaisesRegex(finance.LedgerError, "vinculado duas vezes"):
            finance.reconcile(self.data, statement, "2026-09-25")
        statement["currency"] = "USD"
        with self.assertRaisesRegex(finance.LedgerError, "moeda diferente"):
            finance.reconcile(self.data, statement, "2026-09-25")

    def test_cli_outputs_numbers_without_modifying_fixture(self):
        before = FIXTURE.read_bytes()
        result = subprocess.run([sys.executable, str(ROOT / "scripts" / "finance.py"), str(FIXTURE), "--as-of", "2026-09-25"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["totals"]["cash_balance"], "1700.00")
        self.assertEqual(FIXTURE.read_bytes(), before)

    def test_cli_invalid_input_fails_without_report(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts" / "finance.py"), str(FIXTURE), "--as-of", "2026-08-01"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("anterior ao saldo inicial", result.stderr)


if __name__ == "__main__":
    unittest.main()
