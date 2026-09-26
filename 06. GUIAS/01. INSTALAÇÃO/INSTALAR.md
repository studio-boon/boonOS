# Instalar o boonOS 2.1 (beta)

Você precisa de um agente com acesso à pasta local e acesso à sua conta nesse agente. O pacote inclui contratos para Codex e Claude Code. Git é opcional para baixar o pacote. Ferramentas de imagem, apresentações, serviços externos e rotinas recorrentes são opcionais e dependem do ambiente.

## 1. Escolha a edição certa

**Caminho mais simples, sem terminal:**

1. Se o repositório estiver privado, aceite o convite do GitHub e entre na conta que recebeu acesso.
2. Abra a [release boonOS 2.1](https://github.com/tchelove/boonOS/releases/tag/v2.1.0-beta.1). Em **Assets**, baixe `boonOS-2.1-beta.zip`.
3. Extraia o ZIP em uma pasta sua, por exemplo `Documentos/meu-sistema`. Você pode renomear a pasta.
4. Abra a pasta extraída que contém `AGENTS.md`, `CLAUDE.md` e `boonos.json` — esses arquivos devem estar diretamente dentro dela.

Se preferir baixar o código pelo GitHub, abra a [branch beta/2.1](https://github.com/tchelove/boonOS/tree/beta/2.1) e use **Code → Download ZIP**. Extraia antes de usar. As pastas `.agents` e `.claude` podem estar ocultas na interface do sistema; mantenha-as no pacote.

**Se já usa Git**, clone esta edição explicitamente:

~~~bash
git clone --branch beta/2.1 --single-branch https://github.com/tchelove/boonOS.git meu-sistema
cd meu-sistema
~~~

Clonar sem `--branch beta/2.1` segue a branch padrão do GitHub e pode trazer uma edição posterior. Confira `boonos.json`: esta edição usa a versão `2.1.0-beta.1`.

## 2. Abra no seu agente

Se ainda não tiver um agente instalado, escolha **um** caminho e conclua a instalação e o login da sua conta. Os requisitos e formas de acesso ficam nos guias oficiais:

- **Codex:** [primeiros passos no aplicativo](https://learn.chatgpt.com/docs/quickstart) ou [Codex no terminal](https://learn.chatgpt.com/docs/codex/cli).
- **Claude Code:** [instalação e primeira sessão](https://code.claude.com/docs/en/quickstart).

Não precisa instalar os dois. O boonOS é a pasta de contexto e processos; o agente é o aplicativo que lê e trabalha nela.

| Agente | Entrada local |
|---|---|
| Codex | no aplicativo, use a opção de abrir pasta/projeto e escolha a pasta extraída; no terminal, execute `codex` dentro dela |
| Claude Code | execute `claude` dentro da pasta ou abra-a na interface que utiliza |

A disponibilidade do aplicativo e seus requisitos dependem da plataforma e da versão instalada. A existência dos contratos neste pacote não declara teste real em cada combinação de Windows/macOS e agente.

Na primeira conversa:

> Use a skill local init deste workspace e me guie na configuração. Quero conhecer as possibilidades criativas e operacionais e começar por uma situação minha.

No Codex, `$init` é uma alternativa para selecionar a skill. No Claude, use o pedido explícito acima: `/init` pode ter outro significado no aplicativo. Não é necessário editar YAML para começar.

## 3. Escolha o ritmo

**Primeira missão:** conte uma situação, traga o material mínimo e produza uma saída útil. O agente registra o contexto confirmado no escopo autorizado e deixa o restante para depois.

**Configuração aprofundada:** explore identidade, criação, operação, fontes, ferramentas, critérios e limites em blocos de até três perguntas. Ao pausar, salve um resumo autorizado; a próxima sessão continua por ele.

Em ambos, o resultado é um sistema com o seu contexto e uma próxima ação clara. Leia [Comece aqui](<../../00. COMECE-AQUI.md>) e o [mapa de possibilidades](<../02. POSSIBILIDADES/POSSIBILIDADES.md>).

## 4. Confira a leitura no seu ambiente

Peça ao agente para informar o nome da versão, citar a prioridade de `01. SISTEMA/CONTEXTO.md` e dizer se existe um checkpoint. Num template vazio, ele deve reconhecer que ainda não há prioridade confirmada.

Se não encontrar a skill, confira se abriu a pasta raiz correta e se o arquivo local da skill está presente. Abra uma nova sessão dentro dessa pasta. Se a instalação do agente não carregar skills locais, peça a leitura do `SKILL.md` pelo caminho; isso é um procedimento manual, não prova descoberta automática.

Os verificadores do pacote exigem Python 3.10 ou superior. Na raiz:

~~~bash
python3 scripts/check.py
~~~

No Windows, use `py -3` no lugar de `python3` se esse for o comando disponível. O check estrutural não comprova qualidade das respostas nem funcionamento de integrações. Não é necessário executá-lo para cada conversa.

## 5. Mantenha uma cópia sua

Se for guardar contexto pessoal ou de negócio no GitHub, use um repositório seu e privado. Um clone do template ainda aponta para o repositório de origem; não envie seu contexto para lá. Configure o destino da sua cópia antes do primeiro push.

O botão “Use this template” só serve para esta edição quando a versão desejada estiver incluída na cópia gerada. Confira `boonos.json` depois de criar a cópia. Atualizar uma instalação personalizada exige [migração revisada](ATUALIZAR.md), não substituir a pasta inteira.

Documentos confidenciais ficam em armazenamento com acesso adequado. Não coloque credenciais no perfil. Antes de usar um destino local ignorado, confirme a regra e o rastreamento no Git.
