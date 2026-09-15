# boonOS

Um template de sistema pessoal para criar, estudar e tocar projetos com IA.

O boonOS não é um app, nem uma cópia da operação da BOON. É uma estrutura personalizável de contexto, memória, decisões, projetos e skills. Ele vem com uma curadoria enxuta para alguém aprender fazendo: criar uma ideia, dar direção a uma peça, montar um deck, estudar uma referência, revisar um site ou organizar um case.

> Modelos mudam. Contexto, repertório e boas decisões acumulam valor.

O caminho principal é o Codex. Claude Code continua compatível.

## Comece em 5 minutos

### Opção recomendada: criar uma cópia sua no GitHub

1. Se o repositório estiver marcado como template no GitHub, clique em Use this template e crie um repositório seu. Ele deve ser privado se você for guardar qualquer contexto pessoal, de clientes, contratos ou financeiro.
2. Clone o repositório criado na sua máquina.
3. Abra a pasta no Codex Desktop ou rode Codex CLI nela.
4. Na primeira conversa, escreva $init.

~~~bash
git clone https://github.com/SEU-USUARIO/SEU-SISTEMA.git meu-sistema
cd meu-sistema
codex
~~~

No Codex Desktop, basta abrir essa pasta como workspace e chamar $init.

### Alternativa: clonar este repositório

~~~bash
git clone https://github.com/tchelove/boonOS.git meu-sistema
cd meu-sistema
codex
~~~

Depois, se quiser guardar o seu contexto no GitHub, crie um repositório seu e conecte-o seguindo as instruções do GitHub. Use repositório privado se houver qualquer contexto pessoal, de clientes, financeiro ou documento sensível.

## Pré-requisitos

- [Codex](https://learn.chatgpt.com/docs/codex/cli) no Desktop ou na linha de comando — recomendado;
- Git;
- uma conta com acesso ao Codex;
- opcionalmente, [Claude Code](https://docs.anthropic.com/en/docs/claude-code) para usar o mesmo sistema em outro agente.

## O que o $init faz

O onboarding faz uma entrevista curta e progressiva. Ele pergunta o nome que você quer dar ao seu sistema, seu momento de trabalho e estudo, prioridades, jeito de decidir, referências, voz e os tipos de criação que quer praticar.

Antes de gravar qualquer coisa, ele mostra um resumo para você aprovar. Só depois preenche:

- 01. SISTEMA/CONTEXTO.md — a fonte humana do que importa;
- 01. SISTEMA/PERFIL.yaml — preferências estruturadas, sem segredos;
- 01. SISTEMA/SKILLSET.md — sua trilha e skills prioritárias;
- 01. SISTEMA/ONBOARDING.md — estado e primeira missão;
- 02. MEMORIA/voz-e-estilo.md — quando houver material para isso.

Você pode chamar o sistema de MateusOS, Estúdio X, Laboratório Criativo ou qualquer outro nome. O template se adapta a você; não o contrário.

## Estrutura

~~~text
boonOS/
  AGENTS.md              contrato principal para o Codex
  CLAUDE.md              ponte de compatibilidade para Claude Code
  00. COMECE-AQUI.md     guia humano rápido
  00. TRABALHO/          projetos, rascunhos e entregas em curso
  01. SISTEMA/           contexto, perfil, decisões e skillset
  02. MEMORIA/           aprendizados e preferências que precisam persistir
  03. DOCS/              briefings, estudos, fontes e documentos
  99. OLD/               arquivo recuperável de itens encerrados
  .agents/skills/        skills canônicas do Codex
  .claude/skills/        espelho compatível com Claude Code
  templates/             moldes para transformar decisões em trabalho
  docs/                  instalação, mindset e personalização
~~~

## As 20 skills do pacote

O pacote é deliberadamente curado. Em vez de centenas de comandos, ele traz 20 caminhos que se combinam para aprender, criar e revisar:

| Família | Skills |
|---|---|
| Sistema e clareza | $init, $overview, $router, $skill-creator, $grill-me |
| Estudo e linguagem | $study-playbook, $writing-filter, $copywriting, $brand-storytelling |
| Conteúdo | $content-strategy, $carrossel, $post-social |
| Direção criativa | $design, $design-review, $taste, $image-direction |
| Apresentação e digital | $presentation, $site-design, $interface-polish, $portfolio-case-study |

Elas não carregam clientes, preços, referências proprietárias, voz ou processos internos da BOON. Cada uma lê o seu contexto e usa campos editáveis, para que fique com a sua cara.

Veja o mapa e exemplos em [docs/SKILLS.md](docs/SKILLS.md).

## O mindset

O sistema ensina quatro hábitos simples:

1. Contexto antes de ação: explique a situação, o objetivo e as restrições.
2. Decisão antes de acabamento: registre o que precisa ser percebido antes de escolher cor, texto ou efeito.
3. Skill para o que se repete: uma skill é um jeito reutilizável de pensar, não um botão mágico.
4. Integração e automação só depois: primeiro o fluxo precisa ser entendido, seguro e observável.

Leia [docs/MINDSET.md](docs/MINDSET.md) para ver como isso aparece no trabalho real.

## Segurança e autoria

- O $init não varre o seu computador, Drive ou contas.
- Nenhuma integração, publicação, envio externo ou operação financeira acontece sem pedido e confirmação explícitos.
- Não coloque senhas, tokens, dados bancários ou documentos fiscais no repositório.
- Use 01. SISTEMA/PRIVADO.md para notas locais e 03. DOCS/_PRIVADO/ para documentos locais; ambos já são ignorados pelo Git.
- Arquivo ignorado não é cofre: não coloque senhas, tokens ou dados bancários em texto simples.
- Contexto preenchido pelo usuário é dele. Antes de compartilhar um repositório, revise o que há em 01. SISTEMA, 02. MEMORIA e 03. DOCS.

## Próximos passos

Abra [00. COMECE-AQUI.md](00.%20COMECE-AQUI.md), rode $init e escolha uma primeira missão pequena: recriar uma peça que você admira, estudar um case, organizar uma ideia de portfolio ou montar uma apresentação curta.

Para detalhes:

- [Instalação](docs/INSTALAR.md)
- [Personalização](docs/PERSONALIZAR.md)
- [Mapa das skills](docs/SKILLS.md)
- [Possibilidades e percursos de prática](docs/POSSIBILIDADES.md)
- [Módulos que podem entrar depois](docs/MODULOS-FUTUROS.md)
- [Como atualizar sem apagar seu contexto](docs/ATUALIZAR.md)

Para quem mantém o repositório-base: [checklist de publicação](docs/PUBLICAR.md).
