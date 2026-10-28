# Precificação com premissas

Use as condições da pessoa e do projeto. Não há tabela universal de preço, imposto ou margem no template.

## Entrada mínima

Escopo e exclusões; esforço e prazo; custos diretos; parcela de custos fixos atribuída; risco/retrabalho; moeda; margem pretendida; taxas/provisões informadas e sua base de incidência. Campo desconhecido gera cenário explícito, não zero silencioso.

## Modelo opcional de custo e margem

Se a pessoa adotar percentuais incidentes sobre o preço bruto:

```text
C = custo direto + trabalho próprio custeado + fixo alocado + reserva de risco em valor
T = soma das taxas/provisões sobre preço bruto, como fração
M = margem pretendida sobre preço bruto, como fração
preço = C / (1 - T - M)
```

Condição: `C >= 0`, `0 <= T < 1`, `0 <= M < 1` e `T + M < 1`. Se alguma taxa tiver outra base, a fórmula não serve sem adaptação. Não contar o trabalho próprio duas vezes entre custo e lucro. O piso usa margem mínima escolhida; recomendado e ampliado mudam escopo, risco ou margem com justificativa.

Faça o cálculo com `decimal.Decimal` em Python ou planilha com fórmula visível. Arredonde somente o preço apresentado para centavos e recompute as parcelas para somarem o preço. Não confunda margem sobre venda com markup sobre custo.

## Exemplo inteiramente fictício

Custo `600.00`, taxa informada `0.10` e margem pretendida `0.20`:
`600 / (1 - .10 - .20) = 857.142857...`, apresentado como `857.14`.
Taxas arredondadas `85.71`; contribuição após custo e taxa `171.43`. Esses percentuais demonstram matemática, não recomendação fiscal ou comercial.

## Saída interna

| Cenário | Escopo | C | T e fonte | M e motivo | Preço calculado | Risco/condição |
|---|---|---|---|---|---|---|

Mostrar capacidade de executar, o que muda com desconto e quais dados mudariam a decisão. O usuário decide o preço; a proposta externa recebe apenas condições autorizadas.
