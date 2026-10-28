# Livro gerencial e cálculo verificável

Um único `livro.json` guarda obrigações e eventos, em uma moeda por arquivo. O livro real vive em `04. GESTÃO/02. FINANCEIRO/98. PRIVADO/` ou na fonte protegida escolhida pela pessoa. A biblioteca contém apenas o contrato e exemplos fictícios.

Contas registram fatos e compromissos. O script calcula as visões. Conciliação compara registros com extrato fornecido. Saúde operacional interpreta os resultados. Preparação contábil reúne documentos para revisão.

## Uso

Na raiz do sistema, com Python 3.9 ou posterior:

```sh
python3 scripts/finance.py "06. GUIAS/03. EXEMPLOS/operacao.json" --as-of 2026-09-25
python3 -m unittest discover -s tests -p test_finance.py -v
```

No Windows, use `python` se esse for o comando instalado. O programa lê os arquivos e imprime JSON. Não grava no livro, consulta banco, emite nota, faz cobrança ou efetua pagamento. Erros de validação saem em stderr, código de saída 2 e sem relatório parcial. Valida também registros posteriores ao corte para não esconder inconsistências.

Para um período, calcule nos dois cortes e subtraia apenas movimentos acumulados (`received_net`, `paid_net`, `cash_in`, `cash_out`). Saldo inicial é o começo do dia declarado; movimentos nessa data entram no cálculo. Para o primeiro período, a base de movimentos anterior a essa data é zero. Não subtraia saldos pendentes para chamar o resultado de receita do mês.

## Schema 1

Campos não reconhecidos, IDs duplicados, datas inválidas e valores ausentes causam erro. Valor desconhecido não deve ser inventado para o script passar: mantenha a pendência fora do livro e declare a cobertura incompleta do relatório.

| Bloco/campo | Contrato |
|---|---|
| `schema_version` | inteiro `1` |
| `currency` | rótulo de moeda com 3 letras maiúsculas; todas as linhas usam a mesma moeda, sem conversão |
| `description` | texto opcional do arquivo |
| `opening_cash` | `date`, `amount`, `source`; saldo no começo da data; pode ser negativo |
| `obligations` | array de obrigações |
| `events` | array de liquidações e estornos |

Obrigação:

| Campo | Contrato |
|---|---|
| `id` | texto único e estável neste livro |
| `kind` | `receivable` ou `payable` |
| `state` | `forecast` ou `committed` |
| `issued_on` | data de origem da obrigação/previsão, não a data de importação |
| `committed_on` | obrigatório em `committed`, ausente em `forecast`; antes dessa data, o relatório a mostra como prevista |
| `due_on` | vencimento, nunca anterior à emissão |
| `amount` | string decimal positiva, até 2 casas, como `"1234.56"`; sem moeda, vírgula, separador de milhar ou expoente |
| `description`, `source` | textos obrigatórios; fonte é ID/link/caminho necessário para verificar o fato |
| `project_id`, `party_id` | vínculos opcionais; preservados na passagem comercial para cliente |
| `cancelled_on` | data opcional; a partir dela a obrigação deixa de compor pendências |

Evento:

| Campo | Contrato |
|---|---|
| `id` | ID único e estável da transação; reutilizar na reimportação para detectar duplicata |
| `obligation_id` | obrigação existente e comprometida na data do evento |
| `date` | data da movimentação confirmada, a partir da data inicial do livro |
| `kind` | `settlement` ou `reversal` |
| `amount` | string decimal positiva; direção deriva da obrigação e do tipo de evento |
| `source` | comprovante, linha do extrato ou confirmação explícita atribuída; sem colar dados privados completos |
| `reverses` | ID da liquidação original; obrigatório só para estorno |

Datas usam `AAAA-MM-DD`. Eventos são ordenados pela data; no mesmo dia, vale a ordem do array. Um estorno precisa vir depois da liquidação referenciada. Um recebimento positivo soma caixa; estorno desse recebimento retira caixa. Um pagamento retira caixa; sua devolução soma caixa.

## Regras de integridade

- Pagamentos parciais são eventos distintos na mesma obrigação. O total líquido não pode superar o valor da obrigação em nenhum momento.
- Estornos podem ser parciais, mas a soma dos estornos não ultrapassa a liquidação original. Não estornar um estorno: um novo pagamento é outro evento.
- Cancelar não apaga dinheiro: qualquer liquidação precisa estar integralmente estornada até a data do cancelamento. Uma nota de crédito sem devolução de caixa exige tratamento documentado fora deste schema; não fingir estorno bancário.
- Previsão não aceita liquidação. Aceite com fonte permite indicar `state=committed` e `committed_on`, preservando ID e evidência da mudança.
- Reimportar o mesmo ID falha. IDs diferentes para o mesmo pagamento não são detectados automaticamente; comparar fonte/identificador de origem antes de inserir. O script não é um importador bancário.
- Não apagar eventos confirmados para corrigir o saldo. Use estorno quando dinheiro voltou; para erro de digitação, preservar preimagem e diff, corrigir com fonte e registrar a revisão. O corte de data reconstrói eventos, compromisso e cancelamento; não reconstrói edições antigas de valores ou vencimentos. Preserve snapshots quando isso for necessário.
- Ao começar um livro no meio da operação, registre saldo inicial verificado e apenas o saldo pendente das obrigações anteriores, referenciando o controle anterior. Não reimporte entradas antigas que já compõem esse saldo.

## Saída e significado

Cada obrigação tem dimensões separadas:

- `state`: prevista ou comprometida no corte;
- `validity`: ativa ou cancelada;
- `liquidation`: pendente, parcial ou liquidada;
- `timing`: ainda não vencida, vence hoje, vencida ou não aplicável.

Uma conta pode estar comprometida, parcialmente paga e vencida ao mesmo tempo. Atraso só se aplica a saldo comprometido ativo, com vencimento anterior ao corte. Previsão passada não vira dívida vencida por conta própria.

| Total | Significado |
|---|---|
| `received_net`, `paid_net` | recebimentos/pagamentos acumulados, líquidos de estornos |
| `cash_in`, `cash_out` | entradas/saídas brutas de caixa, incluindo as direções dos estornos |
| `cash_balance` | saldo inicial + entradas − saídas do livro |
| `receivable_committed`, `payable_committed` | saldos de compromissos ativos |
| `receivable_forecast`, `payable_forecast` | previsões separadas |
| `receivable_overdue`, `payable_overdue` | parte vencida dos compromissos; não somar de novo aos totais comprometidos |
| `cash_after_all_commitments` | cenário de liquidação de todos os compromissos; não tem horizonte nem probabilidade e não é dinheiro disponível |

O script não calcula lucro, DRE, impostos, MRR, probabilidade de venda ou saldo bancário autenticado. Esses conceitos precisam de dados e critérios próprios.

## Conciliação

```sh
python3 scripts/finance.py "caminho/livro.json" --as-of 2026-09-25 --statement "caminho/extrato.json"
```

Schema do extrato fornecido:

```json
{
  "schema_version": 1,
  "currency": "BRL",
  "transactions": [
    {"id": "BANCO-001", "date": "2026-09-15", "direction": "in", "amount": "1200.00", "source": "demo:extrato:linha-1", "event_id": "E-001"}
  ]
}
```

`direction` é `in` ou `out`. `event_id` é opcional: com vínculo explícito, data/direção/valor idênticos produzem `matched`; diferença produz `divergence`. Sem vínculo, correspondência exata gera `candidate`, várias geram `ambiguous`, nenhuma gera `unmatched`. Um mesmo evento não pode ser explicitamente vinculado duas vezes. Candidatos continuam pendentes até revisão; o script não escreve os vínculos.

`complete=true` significa que todos os movimentos do livro no intervalo e todas as linhas fornecidas nesse intervalo tiveram correspondência explícita. Isso não comprova que o extrato fornecido está completo, nem autentica banco ou saldo. Taxas, pagamentos agrupados, datas de compensação distintas e várias contas bancárias ficam para revisão manual, sem forçar correspondência pelo valor.
