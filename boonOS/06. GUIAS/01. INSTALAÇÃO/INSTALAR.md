# Instalar o boonOS beta

Você precisa de **um agente de IA capaz de trabalhar com arquivos locais**, instalado no computador, com sua conta conectada e acesso à internet. Codex e Claude Code são dois caminhos possíveis.

Para o uso no dia a dia, a BOON recomenda um plano pago do agente, como **ChatGPT Plus para o Codex** ou **Claude Pro para o Claude Code**. Preços, limites e formas de acesso são definidos pelos fornecedores e podem mudar. O boonOS não exige uma conta Anthropic para quem usa outro agente.

## 1. Instale conversando com a IA

1. Abra o Codex ou o agente que você escolheu no computador.
2. Copie e cole esta mensagem:

~~~text
Instale o boonOS pelo ZIP da branch principal. Extraia preservando os acentos, confira todos os arquivos e, se a verificação falhar, corrija antes de começar. Depois, informe o caminho completo da pasta, explique como reabri-la sem inventar comandos e me ajude a começar: https://github.com/studio-boon/boonOS
~~~

O agente deve baixar o ZIP da branch principal e extrair uma cópia em uma pasta nova, sem substituir arquivos que você já tenha. O ZIP da branch tem uma pasta externa do repositório e, dentro dela, a pasta `boonOS/`: esta é a raiz do sistema, onde `AGENTS.md` e `boonos.json` ficam diretamente. Abra ou copie somente essa pasta interna como sua instalação pessoal. No macOS, alguns descompactadores podem falhar com acentos: o agente pode extrair com Python e verificar a integridade antes de anunciar que terminou. Se a verificação falhar, ele deve corrigir ou explicar o bloqueio. Depois, pode começar a configuração fazendo perguntas sobre você e seu trabalho. Responda no seu ritmo. Você não precisa digitar comandos para começar.

O agente pode pedir que você escolha uma pasta ou conceda acesso à internet e aos arquivos; confira as solicitações do seu ambiente. Um chat sem acesso aos arquivos locais não consegue executar esse mesmo percurso. A experiência pode variar entre agentes e sistemas operacionais.

Se você já tem uma instalação personalizada, abra a pasta que já usa e peça para retomar. Para atualizar essa instalação, siga [Atualizar sem perder seu contexto](ATUALIZAR.md); não substitua a pasta inteira nem use `git pull` sobre ela.

## 2. Se preferir, instale manualmente

**Caminho mais simples, sem terminal:**

1. Abra as [releases do boonOS](https://github.com/studio-boon/boonOS/releases/tag/v0.1.0-beta.8) e escolha o pacote da versão beta.
2. Em **Assets**, baixe `boonOS-beta.zip` e extraia em uma pasta sua, por exemplo `Documentos/meu-sistema`.
3. Abra no agente a pasta extraída que contém `AGENTS.md`, `CLAUDE.md` e `boonos.json` diretamente dentro dela.

Outra opção é acessar o [repositório](https://github.com/studio-boon/boonOS), clicar em **Code → Download ZIP** e extrair o arquivo. Esse download acompanha a branch principal e contém uma pasta externa do repositório: dentro dela, abra ou copie a pasta `boonOS/`, identificada por `AGENTS.md` e `boonos.json`. Para escolher uma edição específica, use a release, cujo ZIP já abre na pasta do sistema. Mantenha também `.agents` e `.claude`, que podem estar ocultas no computador.

**Se já usa Git**, você também pode clonar o repositório. Tenha cuidado: arquivos de perfil, contexto e continuidade são rastreados nesse clone. Eles não são publicados automaticamente, mas podem ser enviados se você fizer push para um repositório público. Uma regra no `.gitignore` não remove o rastreamento de arquivos já rastreados.

~~~bash
git clone https://github.com/studio-boon/boonOS.git meu-sistema
cd meu-sistema/boonOS
~~~

O clone sem branch específica acompanha a branch principal. Para conferir a edição obtida, abra `boonos.json`.

## 3. Abra no seu agente

Se ainda não tiver um agente instalado, escolha **um** caminho e conclua a instalação e o login da sua conta. Os requisitos e formas de acesso ficam nos guias oficiais:

- **Codex:** [baixe o aplicativo](https://chatgpt.com/download/), veja os [primeiros passos](https://learn.chatgpt.com/docs/quickstart) ou use o [Codex no terminal](https://learn.chatgpt.com/docs/codex/cli).
- **Claude Code:** [instalação e primeira sessão](https://code.claude.com/docs/en/quickstart).
- **Gemini CLI:** [instalação oficial](https://geminicli.com/docs/get-started/installation/).

Escolha apenas o agente que pretende usar. O boonOS é a pasta de contexto e processos; o agente é o aplicativo que lê e trabalha nela.

| Agente | Entrada local |
|---|---|
| Codex | no aplicativo, use a opção de abrir pasta/projeto e escolha a pasta extraída; no terminal, execute `codex` dentro dela |
| Claude Code | execute `claude` dentro da pasta ou abra-a na interface que utiliza |
| Gemini CLI | execute `gemini` dentro da pasta; `GEMINI.md` importa o contrato comum |
| Outro agente com arquivos locais | abra a pasta e peça a leitura de `AGENTS.md` e `.agents/skills/init/SKILL.md` |

A disponibilidade do aplicativo e seus requisitos dependem da plataforma e da versão instalada. A existência dos contratos neste pacote não declara teste real em cada combinação de Windows/macOS e agente.

Na primeira conversa depois de abrir a pasta, você pode dizer:

> Me ajude a configurar este sistema e começar por uma situação real do meu trabalho.

Se o agente precisar de uma indicação mais específica, peça para ler `AGENTS.md` e usar a skill local `init`. No Codex, `$init` é uma alternativa; `/init` pode ter outro significado em outros aplicativos. Não é necessário editar YAML para começar.

## 4. Escolha o ritmo

**Primeira missão:** conte uma situação, traga o material mínimo e produza uma saída útil. O agente registra o contexto confirmado no escopo autorizado e deixa o restante para depois.

**Configuração aprofundada:** explore identidade, criação, operação, fontes, ferramentas, critérios e limites em blocos de até três perguntas. Ao pausar, salve um resumo autorizado; na próxima sessão, abra a mesma pasta e peça para retomar.

Em ambos, o resultado é um sistema com o seu contexto e uma próxima ação clara. Leia [Comece aqui](<../../00. COMECE-AQUI.md>) e o [mapa de possibilidades](<../02. POSSIBILIDADES/POSSIBILIDADES.md>).

## 5. Confira a leitura no seu ambiente

Peça ao agente para informar o nome da versão, citar a prioridade de `01. SISTEMA/CONTEXTO.md` e dizer se existe um checkpoint. Num template vazio, ele deve reconhecer que ainda não há prioridade confirmada.

Se não encontrar a skill, confira se abriu a pasta raiz correta e se o arquivo local da skill está presente. Abra uma nova sessão dentro dessa pasta. Se a instalação do agente não carregar skills locais, peça a leitura do `SKILL.md` pelo caminho; isso é um procedimento manual, não prova descoberta automática.

No Gemini CLI, `/memory show` permite conferir o contexto carregado e `/skills list` lista as skills disponíveis. Versões atuais reconhecem `.agents/skills`; confirme no seu ambiente e siga as solicitações de confiança da pasta e ativação da skill. Consulte a documentação oficial de [contexto](https://geminicli.com/docs/cli/gemini-md/) e [skills](https://geminicli.com/docs/cli/skills/). Esta edição inclui a entrada do Gemini, mas não registra um onboarding executado no aplicativo Gemini CLI. Um chat sem acesso local exige anexar o contexto e salvar as saídas manualmente; não oferece a mesma continuidade da pasta aberta.

Os verificadores do pacote exigem Python 3.10 ou superior. Na raiz:

~~~bash
python3 scripts/check.py
~~~

No Windows, use `py -3` no lugar de `python3` se esse for o comando disponível. O check estrutural não comprova qualidade das respostas nem funcionamento de integrações. Não é necessário executá-lo para cada conversa.

## 6. Cuide da sua pasta

A cópia extraída do ZIP não inclui a pasta `.git` nem aponta para um repositório remoto. Isso reduz o risco de enviar seu contexto por um push sem perceber, mas não protege automaticamente o conteúdo do computador, dos serviços de nuvem ou das pessoas com acesso à pasta. O serviço de IA usado também pode processar as informações que você compartilhar; confira suas políticas e permissões.

Se você usa Git e pretende guardar contexto pessoal ou de negócio no GitHub, avalie um repositório seu e privado. Um clone do template ainda aponta para o repositório de origem; não envie seu contexto para lá. Configure o destino da sua cópia antes do primeiro push e confira os arquivos rastreados.

O botão “Use this template” só serve para esta edição quando a versão desejada estiver incluída na cópia gerada. Confira `boonos.json` depois de criar a cópia. Atualizar uma instalação personalizada exige [migração revisada](ATUALIZAR.md), não substituir a pasta inteira.

Documentos confidenciais ficam em armazenamento com acesso adequado. Não coloque credenciais no perfil. Antes de usar um destino local ignorado, confirme a regra e o rastreamento no Git. Para uma instalação que já existe, preserve a pasta e seu histórico: não apague `.git` nem substitua a pasta automaticamente; faça backup e siga a [orientação de atualização](ATUALIZAR.md) quando precisar migrar.
