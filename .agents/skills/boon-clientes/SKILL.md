---
name: boon-clientes
description: >
  Organiza cadastro e onboarding de uma relação de trabalho, ou promove uma oportunidade aceita preservando IDs e histórico. Use para novo cliente, aceite ou continuidade; não presume contrato assinado nem pagamento.
---

# Clientes

Crie continuidade entre comercial e entrega. Cliente, contrato, projeto e pagamento têm estados próprios.

## Fontes e entrada

Leia cadastro/pipeline existentes e a evidência de aceite. Use o [modelo de cliente](<../../../05. BIBLIOTECA/02. OPERACIONAL/CLIENTE.md>) e os [contratos compartilhados](<../../../05. BIBLIOTECA/02. OPERACIONAL/CONTRATOS-OPERACIONAIS.md>). Se a intenção for só organizar um contato, registre como prospect; não exigir contratação para registrar contexto.

## Condução

- Procure a relação por nome e identificador para evitar cadastro repetido. Resolva homônimos com a pessoa.
- Preserve o mesmo ID quando o prospect converter. Registre fonte, autor, data e alcance do aceite, mantendo pendências contratuais e financeiras explícitas.
- Identifique escopo, aprovador, fontes de trabalho e primeiro marco. Reaproveite respostas já fornecidas; peça somente o que muda a próxima ação.
- Crie ou vincule o projeto por `boon-projetos`. O projeto recebe o contexto necessário, não uma cópia de todos os dados pessoais do cadastro.
- Se houver parcelas ou compromissos confirmados, encaminhe à `boon-contas` com fonte. Não criar recebimento por ter havido aceite.
- Atualize o registro comercial; mover ou reorganizar pastas não é necessário para mudar o estágio. Se solicitado, prepare mapa de movimento e preserve histórico.

## Saída e conclusão

Cadastro real em `04. GESTÃO/01. COMERCIAL/98. PRIVADO/CLIENTES.md`, ou fonte autorizada equivalente; projeto em `00. TRABALHO/NN. NOME/PROJETO.md`. O cadastro pode ser enxuto: identidade, contexto, estados, links e próxima ação.

Concluído quando a relação tem identidade única, passagem comercial documentada e onboarding acionável. Manter comunicação de boas-vindas como rascunho se não houver pedido de envio. Não sobrescrever o contexto anterior para fazê-lo parecer um cliente novo.
