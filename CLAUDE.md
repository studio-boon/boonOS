# boonOS — Sistema Pessoal

> Este arquivo é o contexto central do seu sistema. Depois de rodar `/init`, ele vai ser preenchido com a sua realidade. Por enquanto, são só as instruções base.

---

## Quem sou

[Rode `/init` para configurar]

## O que estou construindo

[Rode `/init` para configurar]

## Foco atual

[Rode `/init` para configurar]

## Voz e estilo

[Rode `/init` para configurar ou crie `_02. MEMORIA/voz-e-estilo.md`]

---

## Estrutura do sistema

```
boonOS/
  _00. TRABALHO/     projetos ativos, entregas, ideias em andamento
  _01. SISTEMA/      regras, decisões e padrões do seu OS
  _02. MEMORIA/      contexto vivo — o que não pode morrer entre conversas
  _03. DOCS/         documentos recebidos, contratos, briefings, referências
  _99. OLD/          arquivo de tudo que já foi
```

---

## Como operar

Antes de executar qualquer tarefa, verificar se existe uma skill relevante em `.claude/skills/` ou `.agents/skills/`.

Criar novas skills com `/skill-creator` sempre que uma tarefa se repetir mais de 3 vezes.

Registrar decisões importantes em `_01. SISTEMA/` — não só a decisão, mas o raciocínio por trás.

Manter `_02. MEMORIA/` como o lugar onde o contexto que importa vive. Sem isso, cada conversa começa do zero.

Quando em dúvida sobre onde algo vai, perguntar antes de criar pasta nova.

---

## Skills disponíveis

| Skill | O que faz |
|---|---|
| `/init` | Onboarding — configura o sistema para a sua vida |
| `/overview` | Panorama do que está rolando no OS |
| `/skill-creator` | Cria uma nova skill personalizada |
| `/grill-me` | Stress-testa uma ideia ou plano |
| `/brand-storytelling` | Ajuda a criar narrativa, posicionamento e mensagem de marca |
| `/content-strategy` | Planeja temas, pilares e calendário editorial |
| `/carrossel` | Cria roteiro, copy e direção visual para carrosséis |
