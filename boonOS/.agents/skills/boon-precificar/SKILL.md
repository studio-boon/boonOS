---
name: boon-precificar
description: >
  Calcula cenários de preço com custos, esforço, capacidade, taxas informadas e margem pretendida. Use para quanto cobrar ou avaliar desconto; não aplica tabelas BOON nem inventa parâmetros tributários.
---

# Precificar

Entregue um preço explicável e suas condições, com cálculo reproduzível.

## Fontes e entrada

Use o [modelo de precificação](<../../../05. BIBLIOTECA/02. OPERACIONAL/PRECIFICACAO.md>). Leia escopo, esforço, custos e restrições já disponíveis. Peça apenas dados que mudam o resultado; valores desconhecidos devem aparecer como premissas de cenário, não como fato.

## Condução

1. Definir o que está sendo precificado, unidade/moeda, prazo, dependências e custo de retrabalho. Separar custo de terceiros e trabalho próprio.
2. Confirmar como a pessoa mede custo e margem. O modelo opcional da biblioteca usa custo total dividido por `1 - taxas sobre preço bruto - margem sobre preço bruto`; só usar quando essa base corresponder ao caso.
3. Calcular com `decimal.Decimal` ou planilha de fórmulas visíveis. Conferir denominador positivo, centavos, soma das parcelas e ausência de dupla contagem de custo próprio/fixo.
4. Comparar cenários pelo que muda: escopo, prazo, risco, margem ou condições. Não preencher três preços com multiplicadores arbitrários se só há dados para um.
5. Explicar o que precisaria mudar para caber em orçamento menor e o efeito sobre capacidade. Um valor calculado não confirma demanda nem autorização para conceder desconto.

## Saída e conclusão

Estimativa interna em `04. GESTÃO/01. COMERCIAL/98. PRIVADO/PRECO-ID.md`, vinculada à oportunidade/projeto. Mostrar entradas, fórmula, resultado arredondado, premissas, dados faltantes e recomendação. A versão externa da proposta recebe apenas preço e condições autorizados.

Concluído quando outra pessoa consegue reproduzir os números e identificar o que mudaria a decisão. Taxas são fornecidas e atribuídas; dúvidas sobre obrigações fiscais são encaminhadas ao profissional responsável. O exemplo numérico da biblioteca é fictício, não parâmetro sugerido.
