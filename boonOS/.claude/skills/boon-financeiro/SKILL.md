---
name: boon-financeiro
description: >
  Calcula caixa, recebimentos, pagamentos, compromissos, previsões e vencidos com o script financeiro e data de corte explícita. Use para visão do dinheiro ou fechamento gerencial; não edita lançamentos nem confunde caixa com lucro.
---

# Financeiro

Apresente números calculados a partir de fontes identificadas, com limites claros da cobertura.

## Fontes e entrada

Leia o [contrato financeiro](<../../../05. BIBLIOTECA/02. OPERACIONAL/FINANCEIRO.md>) e obtenha livro, moeda e corte desejado. Se o pedido for de um período, calcular os cortes conforme o contrato; acumulado desde o saldo inicial não é receita do mês.

## Cálculo e leitura

1. Rodar `python3 scripts/finance.py CAMINHO-LIVRO --as-of AAAA-MM-DD`. No Windows, usar `python` se for o comando instalado. Se não houver Python, declarar cálculo não executado e organizar os dados; não afirmar que o script passou.
2. Em erro, explicar o registro inconsistente e encaminhar correção à `boon-contas`; não contornar validação nem esconder linhas.
3. Mostrar caixa do livro, movimentos líquidos, compromissos a receber/pagar, parte vencida e previsões em blocos separados. Valores vencidos já pertencem aos compromissos: não somar duas vezes.
4. Expor origem do saldo inicial e dados ausentes. `cash_after_all_commitments` é cenário sem prazo, não saldo disponível ou previsão de recebimento.
5. Para projeção por horizonte, usar vencimentos dos saldos ativos e premissas explícitas; separar dinheiro contratado de oportunidade. Não inventar probabilidade de conversão.
6. Quando a pergunta for decisão sobre risco/capacidade, entregar dados à `boon-saude-operacional`; quando for documentação do mês, à `boon-contabilidade`.

## Saída e conclusão

Responder com resumo e, quando pedido, salvar `04. GESTÃO/02. FINANCEIRO/98. PRIVADO/RELATORIO-AAAA-MM-DD.md`, com caminho/hash do livro, comando, corte e resultado. O relatório é derivado: o livro continua sendo a fonte.

Concluído quando valores podem ser reproduzidos, período e cobertura estão claros e pendências aparecem. Não chamar fluxo de caixa de lucro/DRE nem afirmar saldo bancário conciliado sem executar a conciliação e confirmar cobertura do extrato.
