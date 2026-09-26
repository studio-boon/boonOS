---
name: boon-fornecedores
description: >
  Compara cotações e organiza compromissos, entregas e pendências de fornecedores. Use para selecionar parceiro, conferir escopo comprado ou acompanhar recebimento; não contrata, compra ou paga automaticamente.
---

# Fornecedores

Compare aquilo que será entregue e mantenha compromisso e recebimento rastreáveis.

## Fontes e entrada

Use o [modelo de fornecedores](<../../../05. BIBLIOTECA/02. OPERACIONAL/FORNECEDORES.md>). Leia necessidade, especificação, prazo e cotações fornecidas. Pesquisa de novos fornecedores só quando fizer parte do pedido; uma cotação vencida precisa ser identificada como tal.

## Condução

- Normalizar escopo comparável: quantidade, qualidade/critério, prazo, revisões, logística, moeda, validade e exclusões. Não esconder diferença de escopo numa comparação por preço.
- Destacar dependências, informação ausente e risco pertinente à entrega. Não inventar capacidade, reputação ou disponibilidade.
- Recomendar opção com motivo e trade-offs, preservando quem decide. Comparação não confirma contratação.
- Após aceite informado, registrar fonte, responsáveis, entregas e obrigações, encaminhando dados ao livro por `boon-contas`. Cotação não aceita permanece previsão.
- Conferir recebimento contra critério e registrar pendência ou aceite atribuído. Entrega e quitação são estados distintos.

## Saída e conclusão

Comparação e registro em `04. GESTÃO/05. FORNECEDORES/98. PRIVADO/FORNECEDORES.md` ou documento do projeto já adotado, com IDs e links. Dados bancários e documentos completos permanecem na fonte protegida.

Concluído quando a escolha/pendência é explicável e o próximo passo tem responsável conhecido. Pedir contato, contratar, comprar e pagar são ações externas específicas; somente executar quando autorizadas e por ferramenta disponível. O pacote base não inclui executor de compra ou pagamento.
