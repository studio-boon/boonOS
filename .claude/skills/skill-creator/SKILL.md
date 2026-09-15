---
name: skill-creator
description: >
  Cria, revisa e testa uma skill pessoal para um fluxo que se repete. Use quando
  a pessoa disser "$skill-creator", "isso devia virar uma skill", "quero um comando
  para isso", "cria uma skill" ou quando um processo recorrente precisar de um
  checklist e uma saída consistente.
---

# skill-creator — transforme repetição em um bom processo

Uma skill não é um atalho para pensar menos. É uma forma de preservar um raciocínio que já funcionou.

## Antes de criar

Confirme que há:

- uma tarefa repetida ou um critério que precisa persistir;
- um gatilho reconhecível;
- uma saída desejada;
- um caso real para testar.

Se for uma tarefa única, use uma skill existente ou faça o trabalho sem criar estrutura permanente.

## Entrevista curta

Pergunte:

1. Em que situação essa skill deve entrar?
2. Quais informações ela precisa antes de agir?
3. Qual saída prova que ela funcionou?
4. O que ela não pode fazer ou assumir?

Busque um fluxo pequeno. Se a descrição depender de muitas exceções, proponha um playbook ou uma etapa manual antes.

## Implementação

Crie primeiro:

~~~text
.agents/skills/[nome-da-skill]/SKILL.md
~~~

O frontmatter mínimo é:

~~~yaml
---
name: nome-da-skill
description: O que ela faz e quando deve ser usada.
---
~~~

Depois escreva:

1. propósito;
2. briefing mínimo;
3. passos na ordem certa;
4. gates de segurança ou qualidade;
5. formato de saída;
6. casos em que deve perguntar ou encaminhar.

Não codifique nomes de clientes, caminhos pessoais, preços, credenciais, voz privada ou fatos que possam mudar.

Quando a skill estiver pronta, espelhe a mesma árvore em .claude/skills/[nome-da-skill]/. A versão em .agents é a canônica.

## Teste

Proponha dois prompts reais: um caso simples e um caso de borda. Rode ou simule os dois, e ajuste a skill somente com evidência do que faltou.

Se scripts/check-skills.sh existir, execute-o depois de mudanças em skills.
