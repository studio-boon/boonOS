# boonOS

Um sistema operacional pessoal que roda no Claude Code.

---

## O que é

boonOS é uma estrutura para você rodar sua vida e seu trabalho com IA — de verdade. Não é um chatbot. Não é um app. É um sistema com memória, decisões, pastas e comandos próprios que evolui à medida que você usa.

A base é simples: pastas, um arquivo de contexto (`CLAUDE.md`), e skills — comandos que você cria para automatizar o que faz com frequência.

Quanto mais contexto você coloca, mais inteligente o sistema fica. Quanto mais você usa, mais você aprende. O sistema melhora porque você melhora.

---

## Pré-requisitos

- [Claude Code](https://claude.ai/code) instalado
- Uma conta Anthropic (plano Pro ou Max recomendado para uso intenso)
- Git instalado

---

## Instalação

```bash
git clone https://github.com/tchelove/boonOS.git
cd boonOS
```

Depois abra a pasta no Claude Code — pelo terminal, pelo VS Code ou pelo app:

```bash
claude  # dentro da pasta boonOS
```

---

## Primeiro passo: `/init`

Antes de qualquer coisa, rode:

```
/init
```

O sistema vai te fazer uma série de perguntas — quem você é, o que você quer organizar, quais são seus objetivos. Com base nas suas respostas, ele configura o `CLAUDE.md` para a sua realidade e indica os primeiros passos reais.

É o único passo obrigatório. Tudo o que vem depois depende de você.

---

## Como o sistema funciona

Cinco pastas. Cada uma com um propósito claro:

| Pasta | Para quê |
|---|---|
| `_00. TRABALHO/` | Projetos ativos, entregas em andamento, ideias que estão rolando |
| `_01. SISTEMA/` | As regras, decisões e padrões do seu OS |
| `_02. MEMORIA/` | Contexto vivo — quem você é, o que importa, histórico que não pode morrer |
| `_03. DOCS/` | Documentos recebidos, contratos, briefings, material de referência |
| `_99. OLD/` | Arquivo — tudo que já foi, sem deletar |

O Claude Code lê o `CLAUDE.md` e navega as pastas quando precisa de contexto. Não é magia: é contexto. Mais contexto = respostas melhores = sistema mais útil.

---

## Como alimentar o sistema

Coloque coisas nas pastas:

- Notas brutas de reuniões → `_00. TRABALHO/`
- Decisões que você toma → `_01. SISTEMA/`
- Contexto sobre você e seus projetos → `_02. MEMORIA/`
- Contratos, orçamentos, briefings → `_03. DOCS/`

O Claude Code lê, pergunta, organiza e vai construindo memória disso. Você não precisa estruturar tudo perfeitamente — pode jogar o texto bruto e pedir para ele organizar.

---

## Como criar uma skill

Skills são comandos personalizados para o que você faz com frequência.

Exemplos do que podem virar skills:
- `/reuniao` — organiza notas brutas de uma call em decisões e próximos passos
- `/projeto` — monta a estrutura de um novo projeto na pasta certa
- `/review` — revisa um texto seguindo o seu tom de voz
- `/semana` — faz o panorama da semana e organiza prioridades

Para criar a sua primeira skill:

```
/skill-creator
```

Descreva o que você quer que o skill faça. O sistema cria o arquivo e você tem um comando novo funcionando.

---

## Skills incluídas

| Skill | O que faz |
|---|---|
| `/init` | Onboarding — configura o sistema para a sua vida |
| `/overview` | Panorama do que está rolando no seu OS |
| `/skill-creator` | Cria uma nova skill personalizada |
| `/grill-me` | Stress-testa uma ideia ou plano — pergunta até esgotar |

---

## Exemplos de uso

**Designer freelancer**
- Usa `/init` para configurar com foco em clientes e projetos criativos
- Cria `/proposta` que gera propostas a partir de notas de reunião
- Alimenta `_02. MEMORIA/` com seu processo, seus clientes, como você trabalha
- Usa `/overview` para ver o status de todos os projetos abertos

**Empreendedor**
- Registra decisões importantes em `_01. SISTEMA/` para o sistema lembrar o raciocínio
- Cria `/pipeline` para acompanhar oportunidades comerciais
- Alimenta o sistema com resumos de calls, e-mails importantes, contexto de reuniões

**Profissional criativo (redator, diretor de arte, produtor)**
- Usa `_00. TRABALHO/` para capturar ideias brutas antes de esquecer
- Cria `/roteiro` que estrutura ideias soltas em conteúdo publicável
- Mantém em `_02. MEMORIA/` o que está aprendendo, quais referências importam, seu ponto de vista

**Estudante ou pesquisador**
- Coloca artigos, anotações e sínteses em `_03. DOCS/`
- Cria `/estudo` que resume e conecta o que leu com o que já sabe
- Usa `/grill-me` para testar argumentos e hipóteses antes de escrever

---

## O que você não vai achar aqui

Não tem interface bonita. Não tem dashboard. Não tem onboarding automático com confete.

boonOS é um sistema que exige que você traga contexto real para funcionar bem. Se você jogar lixo dentro, vai receber lixo de volta. Se você tratar isso como um caderno vivo — onde você registra decisões, projetos, aprendizados, contexto da sua vida — ele vira algo que nenhum app consegue replicar.

A inteligência não vem do sistema. Vem de você.

---

## Créditos

boonOS é um produto interno do [estúdio BOON](https://boonbrands.com.br) adaptado para uso pessoal.

**BOON** é um estúdio de branding estratégico. A gente trabalha com marcas que recusam o óbvio.

- Site: [boonbrands.com.br](https://boonbrands.com.br)
- Instagram: [@boon.brands](https://www.instagram.com/boon.brands)

---

*Feito com Claude Code.*
