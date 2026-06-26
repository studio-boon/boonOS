---
name: init
description: >
  Onboarding do boonOS. Faz uma entrevista para entender quem é o usuário, o que
  ele quer organizar e quais são seus objetivos. Ao final, gera um CLAUDE.md personalizado
  e indica os primeiros passos reais. Use quando o usuário disser "/init", "configura o sistema",
  "começa o onboarding", "inicializa", ou quando o CLAUDE.md ainda tiver campos
  "[Rode `/init` para configurar]".
---

# /init — Onboarding do boonOS

## Propósito

Fazer uma entrevista para calibrar o sistema à realidade do usuário. Ao final, gerar um `CLAUDE.md` personalizado e indicar os próximos passos concretos.

O sistema não serve todo mundo do mesmo jeito. Essa entrevista existe para ele se moldar à pessoa — não o contrário.

## Princípio

Perguntas abertas. Uma de cada vez. Escuta ativa. Nada de suposições sobre o que a pessoa precisa antes de ouvir.

---

## Fluxo

### Fase 1 — Identidade e contexto

Fazer uma pergunta de cada vez. Esperar a resposta antes de continuar.

**Pergunta 1:**
"Antes de qualquer coisa: quem é você? O que você faz no dia a dia?"

Ouvir e anotar: profissão, área, contexto de vida, como trabalha.

**Pergunta 2:**
"O que você quer organizar com esse sistema? Pode ser trabalho, vida pessoal, projetos criativos, estudos, financeiro — qualquer coisa."

Ouvir e anotar: áreas, projetos, tipos de informação que circulam na vida dessa pessoa.

**Pergunta 3:**
"Qual é o seu maior caos agora? O que você mais perde, esquece ou nunca consegue manter no lugar?"

Ouvir e anotar: dores reais, o que não funciona, onde o sistema vai ter mais impacto imediato.

---

### Fase 2 — Objetivos

**Pergunta 4:**
"O que muda na sua vida se daqui a 90 dias esse sistema estiver funcionando bem?"

Ouvir e anotar: objetivo concreto, o que representa "funcionar bem" para essa pessoa.

**Pergunta 5:**
"Você vai usar isso mais para trabalho, para vida pessoal, ou os dois?"

Ouvir e anotar: escopo de uso, frequência esperada.

**Pergunta 6:**
"Tem alguma área específica que você quer resolver primeiro? Um projeto, uma frente, uma parte da vida que tá mais urgente?"

Ouvir e anotar: prioridade imediata, onde começar.

---

### Fase 3 — Modo de uso

**Pergunta 7:**
"Com que frequência você imagina abrir isso? Todo dia, algumas vezes por semana, uma vez por semana?"

Ouvir e anotar: cadência esperada.

**Pergunta 8:**
"Você já usou algum sistema de organização antes — Notion, Obsidian, papel, planilha, nada? O que funcionou? O que não funcionou?"

Ouvir e anotar: histórico, o que repetir, o que evitar.

---

### Fase 4 — Geração

Com base nas 8 respostas, gerar:

#### 1. CLAUDE.md personalizado

Reescrever o arquivo `CLAUDE.md` substituindo os campos `[Rode /init para configurar]` por conteúdo real:

**Quem sou** — síntese em 2–3 parágrafos: identidade, o que faz, como trabalha, o que importa.

**O que estou construindo** — projetos, objetivos de 90 dias, área de foco, o que está tentando chegar.

**Foco atual** — a prioridade imediata que a pessoa mencionou. O que o sistema deve ter na cabeça agora.

**Como operar** — acrescentar 2–3 regras personalizadas baseadas no que a pessoa disse que não funciona ou quer evitar. Exemplo: "Sempre perguntar antes de criar pasta nova", "Não sugerir ferramentas externas, só o que já existe aqui", "Resumir em tópicos, nunca em texto corrido".

Manter a estrutura de pastas e a lista de skills intactas.

Antes de salvar: mostrar o CLAUDE.md gerado e pedir confirmação.

#### 2. Primeiras 3 skills a criar

Sugerir skills específicas baseadas no uso declarado. Para cada uma: nome, o que ela deve fazer, quando usar.

Exemplos de derivação:
- Designer freelancer → `/proposta`, `/briefing`, `/projeto`
- Empreendedor → `/reuniao`, `/pipeline`, `/decisao`
- Redator / criativo → `/roteiro`, `/ideia`, `/review`
- Estudante / pesquisador → `/estudo`, `/resumo`, `/conexao`
- Profissional corporativo → `/semana`, `/reuniao`, `/status`

Perguntar quais dessas fazem sentido e se a pessoa quer criar agora com `/skill-creator`.

#### 3. Próximos 3 passos concretos

Tarefas simples para fazer logo depois do onboarding:

1. Criar o primeiro arquivo em `_02. MEMORIA/` — uma nota sobre quem você é, seus projetos atuais, o que importa saber agora.
2. Criar a primeira skill indicada.
3. Colocar algo real em `_00. TRABALHO/` — um projeto em andamento, uma ideia, uma lista de tarefas.

Apresentar como lista numerada, direto.

---

## Regras

- Perguntar uma coisa de cada vez — nunca listar várias perguntas juntas
- Não presumir o que a pessoa precisa antes de ouvir
- Adaptar o tom à pessoa: mais técnico para devs, mais direto para empresários, mais aberto para criativos
- Gerar o CLAUDE.md só depois de ter respondido todas as perguntas — não adiantar
- Confirmar com a pessoa antes de salvar qualquer arquivo
- Não inventar projetos ou contexto que a pessoa não mencionou
- Se a pessoa der respostas curtas, aprofundar com uma pergunta de follow-up antes de avançar
