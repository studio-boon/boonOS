---
name: skill-creator
description: >
  Cria novas skills, modifica e melhora skills existentes. Use quando o usuário
  quiser criar um comando personalizado ("quero um skill que...", "/skill-creator",
  "cria uma skill para X", "como crio um comando pra isso?", "isso deveria virar
  uma skill", ou quando uma tarefa se repetir mais de 3 vezes e valer automatizar).
---

# /skill-creator

Uma skill para criar skills — e melhorá-las com o tempo.

---

## Processo

### 1. Capturar a intenção

Entender o que o usuário quer. A conversa atual pode já conter um fluxo que ele quer capturar. Se sim, extrair dali: as etapas, o que funcionou, o formato de saída.

Perguntar:
1. O que esse skill deve permitir fazer?
2. Quando ele deve ser acionado? (quais frases ou contextos)
3. Qual o formato de saída esperado?

### 2. Entrevistar e pesquisar

Fazer perguntas sobre casos de borda, exemplos reais, critérios de sucesso. Não começar a escrever antes de entender bem o uso.

### 3. Escrever o SKILL.md

Criar o arquivo em `.claude/skills/[nome-da-skill]/SKILL.md` com:

```yaml
---
name: nome-da-skill
description: >
  O que o skill faz e quando deve ser acionado. Incluir frases típicas que o usuário
  diria para acionar esse skill. Ser específico — a descrição é o gatilho principal.
---
```

Seguido das instruções em markdown: o que fazer, como fazer, em que ordem, com quais regras.

Se a pasta `.agents/skills/` existir, espelhar a mesma skill em `.agents/skills/[nome-da-skill]/SKILL.md` para manter compatibilidade com outros agentes.

### 4. Testar

Sugerir 2–3 prompts realistas para testar a skill. Pedir ao usuário para confirmar se fazem sentido.

Rodar e avaliar juntos: o resultado foi o esperado? O que ajustar?

### 5. Iterar

Refinar com base no feedback. Repetir até funcionar bem.

---

## Anatomia de uma skill

```
.claude/skills/
└── nome-da-skill/
    ├── SKILL.md          (obrigatório — instrução e frontmatter)
    └── references/       (opcional — docs, exemplos, templates)
        └── exemplo.md

.agents/skills/
└── nome-da-skill/
    └── SKILL.md          (espelho opcional para agentes compatíveis)
```

- Manter o `SKILL.md` claro e direto — idealmente abaixo de 300 linhas
- Usar o frontmatter `description` para descrever quando acionar, não só o que faz
- Se o skill tiver múltiplas variantes, usar subpastas em `references/`

---

## Guia de escrita

- Usar forma imperativa nas instruções: "Perguntar X", "Listar Y", "Gerar Z"
- Explicar o porquê de regras importantes — não só o que fazer
- Incluir exemplos de input/output quando ajudar a clareza
- Evitar instruções genéricas demais — quanto mais específico o contexto, mais útil a skill

---

## Regras

- Não criar skill sem entender o caso de uso real
- Não assumir que o usuário quer evals ou benchmarks — só sugerir se fizer sentido
- Se o usuário disser "faz rápido, sem testar", criar e entregar — sem enrolação
- A skill não está pronta até o usuário confirmar que funciona como esperado
