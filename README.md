# boonOS 2.1 (beta)

Um sistema pessoal de trabalho com IA: para criar, organizar a operação e aprender com o que você faz.

O boonOS reúne contexto, projetos, memória e skills em uma pasta sua. Você conversa com o agente, traz uma situação real e constrói o sistema a partir dela. Ele pode receber outro nome, acompanhar um profissional independente ou ajudar um pequeno time.

## Duas áreas, um contexto

| Área | Você pode pedir | O que recebe |
|---|---|---|
| **Criativo** | “Preciso apresentar essa ideia”; “me ajuda a melhorar esta peça” | narrativa, texto, direção visual, revisão, conteúdo, sites e cases |
| **Operacional** | “Minha semana está confusa”; “quero entender o caixa deste projeto” | planos, responsáveis, propostas, cenários de preço, contas, conciliação e organização contábil |
| **Base compartilhada** | “Me situa”; “quero parar de repetir esse erro” | contexto preservado, caminhos de trabalho, aprendizado e melhorias verificáveis |

Um projeto tem o mesmo briefing, responsável e histórico nas duas áreas. O pacote inclui **40 skills: 14 criativas, 14 operacionais e 12 compartilhadas**. Você usa as que ajudam no momento; não precisa decorar comandos.

Uma skill orienta um processo. Gerar uma imagem, exportar slides ou conectar um serviço depende das ferramentas disponíveis no seu agente. O núcleo trabalha com conversa e arquivos locais; nenhuma conta externa ou rotina recorrente vem ativada.

## Comece pela sua situação

**Sem terminal:** baixe `boonOS-2.1-beta.zip` na [release 2.1](https://github.com/tchelove/boonOS/releases/tag/v2.1.0-beta.1), extraia e abra a pasta no seu agente. Se o repositório estiver privado, aceite primeiro o convite de acesso. O [guia de instalação](<06. GUIAS/01. INSTALAÇÃO/INSTALAR.md>) acompanha cada passo.

**Com Git instalado:** clone esta edição explicitamente:

~~~bash
git clone --branch beta/2.1 --single-branch https://github.com/tchelove/boonOS.git meu-sistema
cd meu-sistema
~~~

Abra a pasta no agente que você utiliza, com acesso à sua conta: Codex ou Claude Code. Na linha de comando, execute `codex` **ou** `claude` dentro dela. Em um aplicativo que permita abrir uma pasta local, selecione `meu-sistema`.

Comece com esta mensagem:

> Me guia na configuração deste sistema. Quero entender o que ele pode fazer e começar por um problema real meu. Use a skill local init.

O onboarding oferece dois ritmos: **resolver uma primeira missão** ou **aprofundar a configuração**. Ele pergunta em blocos curtos, mostra possibilidades criativas e operacionais, confirma o que entendeu e registra apenas o contexto autorizado. Você pode pausar e retomar pelo resumo salvo.

O contrato local usa `AGENTS.md` e `.agents/skills` no Codex; `CLAUDE.md` encaminha para o mesmo contexto e `.claude/skills` no Claude Code. A presença desses arquivos não comprova teste em toda versão ou sistema operacional. O [guia de instalação](<06. GUIAS/01. INSTALAÇÃO/INSTALAR.md>) explica como conferir a leitura no seu ambiente.

## Onde cada coisa fica

~~~text
00. TRABALHO/       projetos e entregas em andamento
01. SISTEMA/        contexto, perfil, regras e estado do sistema
02. MEMORIA/        aprendizados e preferências com origem
03. DOCS/           fontes recebidas e índices de documentos
04. GESTÃO/         comercial, financeiro, contabilidade, rotina e fornecedores
05. BIBLIOTECA/     modelos criativos, operacionais e de evolução
06. GUIAS/          instalação, possibilidades e exemplos
99. ARQUIVO/        histórico recuperável do que saiu de uso
~~~

As pastas organizam o uso. `.agents`, `.claude` e `scripts` guardam os recursos técnicos. Crie projetos e registros quando houver conteúdo para eles; o onboarding não precisa preencher todas as áreas.

## O sistema melhora pelo uso

Uma entrega ou dificuldade pode virar um aprendizado, uma proposta de ajuste e um teste. Se o ajuste funciona, ele entra no sistema com origem e histórico. Se piora o resultado, pode ser revertido.

Esse ciclo acontece durante as sessões. Trabalhar entre sessões exige configurar e verificar um executor recorrente. Uma skill de automação ajuda a preparar essa rotina; não a mantém funcionando sozinha.

## Seu contexto continua sendo seu

Use uma cópia privada se for versionar informações pessoais ou de negócio. Guarde documentos confidenciais em um local com acesso adequado e mantenha aqui apenas as referências necessárias. `98. PRIVADO/` e `01. SISTEMA/PRIVADO.md` são destinos locais previstos nas regras de exclusão; antes de colocar conteúdo neles, confirme que o Git os ignora e que não estão rastreados. Exclusão do Git não é proteção de acesso nem remoção de histórico.

O agente respeita autorizações já dadas para a tarefa. Preparar uma proposta, uma mensagem ou um controle local não autoriza enviar, publicar, pagar ou conectar uma conta. Essas ações precisam estar explicitamente incluídas no pedido ou em uma autorização vigente.

## Continue por aqui

- [Comece aqui](<00. COMECE-AQUI.md>): da pasta aberta à primeira missão.
- [O que posso fazer?](<06. GUIAS/02. POSSIBILIDADES/POSSIBILIDADES.md>): quero → trago → recebo.
- [Mapa das 40 skills](<06. GUIAS/02. POSSIBILIDADES/SKILLS.md>): capacidades, entradas e resultados.
- [Personalizar](<06. GUIAS/02. POSSIBILIDADES/PERSONALIZAR.md>): voz, operação e prioridades.
- [Ferramentas e extensões](<06. GUIAS/02. POSSIBILIDADES/MODULOS-FUTUROS.md>): o que depende de configuração.
- [Atualizar uma instalação](<06. GUIAS/01. INSTALAÇÃO/ATUALIZAR.md>): preservar contexto e personalizações.

Para manter o pacote: [publicar uma versão](<06. GUIAS/01. INSTALAÇÃO/PUBLICAR.md>). Esta é a edição **2.1 beta**, identificada como `v2.1.0-beta.1`.
