---
name: compactar-contexto
description: >
  Cria um checkpoint humano, curto e retomável do trabalho em andamento. Use quando
  a pessoa disser "$compactar-contexto", "compacta o contexto", "salva um resumo",
  "vou abrir outro chat", "quero pausar" ou pedir um handoff para continuar depois
  sem perder decisões, arquivos, limites e próximo passo.
---

# compactar-contexto — checkpoint para retomar sem recomeçar

Esta skill compacta o **estado de trabalho** em um registro legível. Ela não reduz
arquivos por linguagem telegráfica, não substitui documentos-fonte e não controla a
compactação interna da janela de contexto do agente.

## O que ler

Leia `AGENTS.md`, `01. SISTEMA/CONTINUIDADE.md` e as fontes diretamente ligadas ao
trabalho atual. Consulte contexto, decisões, memória e projeto somente na medida
necessária para resolver ambiguidades. Preserve nomes, números, datas e caminhos
exatos.

## Montar o checkpoint

Registre apenas o que permite continuar com segurança:

1. **Escopo e objetivo atual** — o resultado que ainda está sendo perseguido.
2. **Fatos verificados** — cada fato com sua fonte ou caminho.
3. **Decisões e autorizações vigentes** — inclusive o que não foi autorizado.
4. **Artefatos e estado** — criado, candidato, aprovado, enviado, publicado ou
   validado são estados separados.
5. **Restrições e riscos** — privacidade, dependências, gates e conflitos.
6. **Pendências** — perguntas ou verificações que realmente bloqueiam o próximo passo.
7. **Próxima ação exata** — uma ação concreta e o arquivo de onde retomar.

Atualize `01. SISTEMA/CONTINUIDADE.md` quando a pessoa pedir para salvar, compactar,
pausar ou preparar outro chat. Faça uma substituição cirúrgica do checkpoint vigente;
o histórico detalhado continua nos projetos, decisões, memória e fontes apontadas.

## O que não fazer

- Não reescreva `CONTEXTO.md`, `AGENTS.md`, fontes ou memória inteira para economizar
  tokens.
- Não apague o checkpoint anterior antes de conferir que a nova versão preserva
  decisões, limites e caminhos necessários.
- Não inclua segredos, dados privados completos ou uma transcrição integral.
- Não transforme inferência, sugestão ou nome de pasta em fato confirmado.
- Não afirme que a compactação nativa do agente foi executada. Em ambientes que
  oferecem `/compact` ou compactação automática, esse recurso pode ser usado depois;
  o checkpoint do boonOS continua sendo a camada portátil e legível.

## Saída

Além do arquivo atualizado, devolva no chat um handoff curto:

```text
Checkpoint: [escopo]
Estado: [onde parou]
Retomar por: [caminho]
Próxima ação: [ação]
Não comprovado: [efeitos externos ou lacunas relevantes]
```

Para retomar em outra sessão, peça ao agente para ler `AGENTS.md` e
`01. SISTEMA/CONTINUIDADE.md` antes de continuar.
