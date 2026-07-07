# boonOS

Um template simples para criar um sistema operacional pessoal com IA usando pastas, memória e skills.

boonOS não é um app. É uma estrutura de trabalho para usar com Claude Code, Codex ou outro agente compatível com skills locais. Ele dá um lugar claro para projetos, decisões, documentos, contexto e comandos personalizados.

## Para Compartilhar

Mande este bloco para alguém instalar:

```bash
git clone https://github.com/tchelove/boonOS.git meu-boonos
cd meu-boonos
claude
```

Dentro do Claude Code, a primeira mensagem deve ser:

```text
/init
```

O `/init` entrevista a pessoa, personaliza o `CLAUDE.md` e indica os primeiros passos.

## Pré-Requisitos

- [Claude Code](https://claude.ai/code) instalado
- Conta Anthropic ativa
- Git instalado
- Opcional: VS Code, GitHub Desktop ou GitHub CLI para versionar o próprio sistema

## Instalação

Clone o template:

```bash
git clone https://github.com/tchelove/boonOS.git meu-boonos
cd meu-boonos
```

Abra a pasta no Claude Code:

```bash
claude
```

Se quiser usar outro nome de pasta:

```bash
git clone https://github.com/tchelove/boonOS.git nome-do-seu-sistema
cd nome-do-seu-sistema
claude
```

## Primeiro Uso

Rode:

```text
/init
```

O agente vai perguntar:

- quem você é;
- o que você quer organizar;
- qual é o caos principal agora;
- o que precisa estar funcionando em 90 dias;
- como você pretende usar o sistema.

No final, ele atualiza `CLAUDE.md`, sugere primeiras skills e aponta três ações práticas.

## Estrutura

```text
boonOS/
  CLAUDE.md          contexto central que o agente lê primeiro
  README.md          tutorial de instalação e operação
  .claude/skills/    skills para Claude Code
  .agents/skills/    espelho das skills para agentes compatíveis
  _00. TRABALHO/     projetos ativos, entregas, ideias em andamento
  _01. SISTEMA/      regras, decisões e padrões do seu OS
    SKILLSET.md      manifesto do pacote inicial de skills
  _02. MEMORIA/      contexto vivo que não pode morrer entre conversas
  _03. DOCS/         documentos, contratos, briefings e referências
  _99. OLD/          arquivo de versões antigas e projetos encerrados
```

## Caminhos

| Caminho | Use para |
|---|---|
| `CLAUDE.md` | Explicar quem você é, o que está construindo e como o agente deve operar |
| `_00. TRABALHO/` | Guardar projetos ativos, notas brutas e entregas em andamento |
| `_01. SISTEMA/` | Registrar decisões, regras, padrões e mudanças do sistema |
| `_01. SISTEMA/SKILLSET.md` | Ver quais skills vêm instaladas e quais não fazem parte do template |
| `_02. MEMORIA/` | Guardar contexto sobre você, projetos, pessoas, aprendizados e preferências |
| `_03. DOCS/` | Guardar documentos recebidos, materiais de estudo, briefings e referências |
| `_99. OLD/` | Arquivar o que saiu de uso sem deletar histórico |
| `.claude/skills/` | Comandos usados pelo Claude Code |
| `.agents/skills/` | Cópia das skills para outros agentes que leem esse padrão |

## O Que Fazer Depois Do `/init`

1. Crie `_02. MEMORIA/sobre-mim.md` com contexto real sobre você.
2. Coloque um projeto ativo em `_00. TRABALHO/`.
3. Registre uma decisão importante em `_01. SISTEMA/`.
4. Rode `/overview` para ver se o sistema entendeu o estado atual.
5. Quando repetir uma tarefa 3 vezes, crie uma skill com `/skill-creator`.

## Skills Incluídas

| Skill | O que faz |
|---|---|
| `/init` | Faz o onboarding e personaliza o sistema |
| `/overview` | Gera panorama do que existe nas pastas e próximos passos |
| `/skill-creator` | Cria ou melhora skills personalizadas |
| `/grill-me` | Questiona uma ideia, plano ou decisão até ficar mais clara |
| `/brand-storytelling` | Ajuda a construir narrativa, posicionamento e mensagem de marca |
| `/content-strategy` | Planeja conteúdo, pilares, temas e calendário editorial |
| `/carrossel` | Cria estrutura, roteiro, copy e direção visual para carrosséis |

O template não inclui um filtro de linguagem fixo. A voz deve ser definida pelo usuário em `CLAUDE.md` ou em um arquivo como `_02. MEMORIA/voz-e-estilo.md`.

## Como Usar No Dia A Dia

Use linguagem simples. Exemplos:

```text
/overview
```

```text
Organiza essas notas de reunião dentro de _00. TRABALHO/[nome-do-projeto].
```

```text
Registra essa decisão em _01. SISTEMA e guarda o raciocínio.
```

```text
Cria um carrossel de 7 slides sobre [tema] para [público].
```

```text
Isso aqui virou uma tarefa recorrente. Cria uma skill para eu repetir esse fluxo.
```

## Personalização De Voz

Depois do `/init`, crie ou peça para o agente criar:

```text
_02. MEMORIA/voz-e-estilo.md
```

Inclua:

- como você gosta de escrever;
- palavras que usa e palavras que evita;
- exemplos de textos seus;
- referências de tom;
- regras para posts, propostas, estudos ou mensagens.

As skills de conteúdo devem respeitar essa memória. Sem esse arquivo, elas usam um tom claro e neutro.

## Criando Seu Próprio Repositório

Se você quer transformar o template em um repo seu, faça isso depois de clonar:

```bash
rm -rf .git
git init
git add .
git commit -m "init personal os"
```

Depois crie um repositório vazio no GitHub e conecte:

```bash
git remote add origin https://github.com/SEU-USUARIO/SEU-REPO.git
git branch -M main
git push -u origin main
```

Use repositório privado se você vai guardar informações pessoais, clientes, contratos, financeiro ou documentos sensíveis.

## Como Criar Skills

Rode:

```text
/skill-creator
```

Boas candidatas a skill:

- tarefa que você já repetiu 3 vezes;
- formato que sempre precisa sair igual;
- checklist que você sempre esquece;
- análise que depende de várias etapas;
- tipo de conteúdo que você cria com frequência.

Exemplos:

| Skill | Função |
|---|---|
| `/reuniao` | Transformar notas de reunião em decisões, tarefas e próximos passos |
| `/proposta` | Montar proposta a partir de briefing |
| `/semana` | Organizar prioridades da semana |
| `/estudo` | Resumir e conectar materiais de estudo |
| `/review` | Revisar texto com a sua voz |

## Atualizando O Template

Se você ainda estiver usando este repo como clone do template:

```bash
git pull
```

Se você já transformou em repo próprio, copie manualmente apenas o que fizer sentido, principalmente novas skills.

## Problemas Comuns

| Problema | Como resolver |
|---|---|
| A skill não aparece | Reinicie o Claude Code dentro da pasta e confira se existe `SKILL.md` dentro da pasta da skill |
| O agente não sabe nada sobre você | Rode `/init` e alimente `_02. MEMORIA/` |
| Está criando pastas demais | Registre uma regra em `_01. SISTEMA/` dizendo para perguntar antes de criar caminhos novos |
| A escrita não parece sua | Crie `_02. MEMORIA/voz-e-estilo.md` com exemplos reais |
| O sistema ficou bagunçado | Rode `/overview`, peça diagnóstico e arquive o que não está ativo em `_99. OLD/` |

## Regra Principal

O sistema só fica útil quando recebe contexto real. Guarde decisões, projetos, notas, documentos e preferências nos caminhos certos. O agente trabalha melhor quando sabe onde procurar.

## Créditos

boonOS nasceu como um sistema interno do estúdio BOON e foi adaptado como template pessoal.

- Site: [boonbrands.com.br](https://boonbrands.com.br)
- Instagram: [@boon.brands](https://www.instagram.com/boon.brands)
