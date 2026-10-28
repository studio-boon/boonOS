---
name: atualizar
description: >
  Reconcilia o contexto, a memória, os projetos e as capacidades do workspace com
  o que os arquivos realmente mostram. Use quando a pessoa disser "$atualizar",
  "atualiza meu sistema", "varre o workspace", "reconcilia a memória" ou pedir
  uma revisão geral antes de continuar. Não substitui a migração de versão do template.
---

# atualizar — manter o sistema coerente

Atualizar é comparar o que o sistema diz com o que as fontes locais comprovam. O
objetivo é reduzir contexto vencido sem transformar hipótese em fato nem reorganizar
o workspace por impulso.

## Antes de começar

Leia `AGENTS.md` e os arquivos de `01. SISTEMA` indicados ali. Consulte
`01. SISTEMA/CONTINUIDADE.md` e apenas os projetos, registros e memórias pertinentes
ao pedido. Use `01. SISTEMA/CATALOGO.json` e `SKILLSET.md` quando a divergência
envolver capacidades.

Esta skill atualiza o conteúdo da instalação. Para instalar uma nova edição do
boonOS, siga `06. GUIAS/01. INSTALAÇÃO/ATUALIZAR.md`: a migração preserva a origem e
não equivale a reconciliar memória.

## Reconciliação

1. Defina o escopo e a data de corte: sistema inteiro, projeto, operação, memória ou
   skills. Uma varredura geral continua limitada aos arquivos locais autorizados.
2. Levante as fontes atuais. Para cada ponto, registre caminho e estado observado;
   nomes como `final`, `pronto` ou `aprovado` não bastam como evidência.
3. Compare fontes com `CONTEXTO.md`, `PERFIL.yaml`, `DECISOES.md`,
   `CONTINUIDADE.md`, `SKILLSET.md`, `02. MEMORIA` e registros do projeto aplicável.
4. Classifique cada diferença como:
   - **desatualização comprovada**: a fonte atual contradiz o resumo;
   - **lacuna**: o sistema não registra algo confirmado e útil;
   - **conflito**: duas fontes relevantes divergem;
   - **proposta**: melhoria ainda sem decisão ou evidência suficiente.
5. Se o pedido autorizou atualizar, faça patches pequenos nos donos corretos da
   informação. Preserve campos pessoais, autoria, datas, IDs, links e histórico.
   Se o pedido foi só conferir, entregue o diagnóstico sem escrever.
6. Verifique links, JSON/YAML e a estrutura afetada. Para mudanças em skills, use
   `boon-gerir-skills`; para alterar um procedimento com histórico e rollback, use
   `boon-melhorar-sistema`.

## Limites

- Não invente prioridade, aprovação, pagamento, envio, publicação, sincronização ou
  funcionamento externo.
- Não copie conversas inteiras, documentos privados ou segredos para a memória.
- Não mova, renomeie, arquive, compacte nem apague arquivos sem autorização explícita
  para essa ação material.
- Não substitua uma fonte detalhada por um resumo. A memória aponta para a fonte.
- Não use `git pull` sobre uma instalação personalizada para fazer migração de versão.

## Saída

Entregue:

- escopo e fontes verificadas;
- fatos atualizados, com os arquivos alterados;
- conflitos e lacunas que continuam abertos;
- validações executadas e o que elas não comprovam;
- próximo passo curto.

Se nada divergir, diga que o escopo verificado está coerente e cite a data de corte.
