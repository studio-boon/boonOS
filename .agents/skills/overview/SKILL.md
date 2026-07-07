---
name: overview
description: >
  Gera um panorama do que está acontecendo no sistema pessoal: projetos ativos,
  pendências, contexto e próximos passos. Use quando o usuário disser "overview",
  "/overview", "o que tá rolando", "me dá um resumo", "como tá tudo", "status geral",
  "o que eu tenho aqui", "me situa".
---

# /overview — Panorama do sistema

## Workflow

### 1. Levantamento

Ler e listar:
- `CLAUDE.md` — quem é o usuário, o que está construindo, foco atual
- `_00. TRABALHO/` — listar o que existe, notar datas de modificação recentes
- `_01. SISTEMA/` — decisões e regras registradas
- `_02. MEMORIA/` — contexto vivo atual

### 2. Montar o panorama

```
## boonOS — Overview [data]

### Em andamento
- [projeto/área] — [status ou última atualização]

### Pausado ou esperando
- [o que está parado e por quê, se houver]

### Última decisão registrada
- [última coisa em _01. SISTEMA/, se houver]

### O que vem a seguir
[Derivar do que está mais próximo de avançar, mais próximo de vencer prazo,
ou do que aparece como próximo passo nos arquivos mais recentes]
```

### 3. Sinalizar gaps

Se detectar:
- `_02. MEMORIA/` vazia — "Você ainda não alimentou a Memória. Sem isso, cada conversa começa do zero. O primeiro arquivo pode ser uma nota sobre você e seus projetos atuais."
- `CLAUDE.md` ainda com campos `[Rode /init para configurar]` — "O sistema ainda não foi personalizado. Rode `/init` para começar."
- Nenhuma atividade recente em `_00. TRABALHO/` — "Nada novo em TRABALHO há um tempo. Tem algo rolando que ainda não entrou aqui?"
- `_01. SISTEMA/` vazia — "Nenhuma decisão registrada ainda. Quando você tomar uma decisão importante, guarda aqui."

## Regras

- Basear em evidências das pastas — não inventar
- Ser direto e curto — é um painel, não um relatório
- Se o sistema estiver vazio demais, dizer o que falta e o que fazer primeiro
- Não romantizar o que está vazio — só sinalizar e indicar próximo passo
