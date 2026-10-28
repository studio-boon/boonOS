# boonOS Beta

Sua IA conhece a tarefa. O boonOS ajuda ela a conhecer **você, seu trabalho e o seu jeito de criar**.

É um sistema que reúne contexto, memória e skills em uma pasta sua. Você configura aos poucos, trabalha em projetos reais e retoma com o que ficou salvo. Foi criado pela BOON a partir do jeito que usamos IA no estúdio.

## Comece por aqui

Você precisa de um computador e de uma IA que trabalhe com arquivos. Recomendamos o **Codex** ou o **Claude Code**, com um plano pago para ter mais disponibilidade.

Abra o agente, copie e cole:

```text
Instale o boonOS e me ajude a começar: https://github.com/studio-boon/boonOS/archive/main.zip
```

A IA vai preparar uma cópia para você e começar uma conversa sobre seu trabalho. Você pode partir de uma tarefa real ou configurar o sistema com mais calma. Não precisa saber comandos: acompanhe as perguntas e as permissões que aparecerem.

**Já tem o boonOS?** Abra a pasta que você já usa e peça para retomar. Para atualizar sem perder seu contexto, siga o [guia de atualização](<06. GUIAS/01. INSTALAÇÃO/ATUALIZAR.md>).

<details>
<summary>Instruções para o agente que está instalando</summary>

Para uma nova instalação, baixe o [ZIP da versão atual](https://github.com/studio-boon/boonOS/archive/main.zip) diretamente pelo endereço do prompt, extraia em uma pasta nova escolhida com a pessoa e preserve os arquivos e pastas ocultos, incluindo `.agents` e `.claude`. Use uma cópia sem `.git`. Não apague nem sobrescreva uma instalação existente. Abra a raiz extraída, leia `AGENTS.md` e use a skill local `init` para começar a configuração. Se a pessoa já tiver uma instalação personalizada, abra a pasta existente e retome o contexto salvo em vez de reiniciar.

</details>

[Prefere instalar manualmente? Veja o passo a passo.](<06. GUIAS/01. INSTALAÇÃO/INSTALAR.md>)

## Como funciona

<picture>
  <source media="(max-width: 600px)" srcset="assets/boonos-como-funciona-mobile.svg">
  <img src="assets/boonos-como-funciona.svg" width="100%" alt="Você e seu agente de IA trabalham em uma pasta boonOS com projetos, contexto, memória e skills; com sua orientação, o feedback também pode gerar melhorias no sistema.">
</picture>

A pasta reúne **seus projetos**, o **contexto** do seu trabalho, a **memória** que vocês registram e as **skills**, que orientam a IA em diferentes tarefas. Na próxima conversa, abra essa mesma pasta para o agente consultar o que já foi salvo.

O boonOS não depende de você explicar tudo de novo a cada conversa. A retomada depende do que foi registrado e do acesso do agente à pasta. Você confere o que será salvo e pode ajustar esse contexto ao longo do uso. [Entenda memória e continuidade](<02. MEMORIA/README.md>).

Com o tempo, aprendizados e feedback podem virar ajustes em processos e instruções, dentro do que você autorizar. Depois, você pode avaliar se a mudança ajudou. [Veja como funciona a melhoria](<01. SISTEMA/APRENDIZADO.md>).

## O que dá pra fazer?

Traga uma ideia, um projeto ou um problema do seu dia a dia. Por exemplo:

- **Criar e comunicar:** desenvolver uma ideia, escrever um roteiro, revisar uma apresentação ou planejar um site.
- **Organizar o trabalho:** estruturar projetos, acompanhar decisões, montar propostas e planejar a semana.
- **Conhecer melhor o negócio:** organizar informações, estudar referências e trabalhar cenários de preço ou caixa.

O pacote reúne **42 skills** com processos criativos e operacionais. Você pode pedir em linguagem comum; o agente usa as instruções pertinentes ao que vocês estão fazendo. As skills orientam o trabalho. Gerar imagens ou vídeos, publicar, conectar serviços e criar automações depende das ferramentas, permissões e configurações disponíveis no seu agente.

## Seu contexto é seu

A instalação recomendada cria uma cópia pessoal em uma pasta sem histórico Git. Essa pasta pode conter informações sobre você e seu negócio: escolha onde guardá-la e quem pode acessá-la. O agente e os serviços de IA usados por você podem processar os arquivos conforme suas próprias configurações e políticas.

Se você usar Git, cuidado antes de enviar alterações: alguns arquivos de contexto são rastreados no repositório. Apenas adicionar uma regra ao `.gitignore` não deixa de rastreá-los. Um clone não publica dados por conta própria, mas um envio posterior para um repositório público pode expô-los. Nunca coloque senhas ou chaves no contexto.

## Continue explorando

- [Comece aqui](<00. COMECE-AQUI.md>): da primeira conversa à primeira missão.
- [O que posso fazer?](<06. GUIAS/02. POSSIBILIDADES/POSSIBILIDADES.md>): ideias de pedidos e resultados.
- [Mapa das skills](<06. GUIAS/02. POSSIBILIDADES/SKILLS.md>): conheça os processos incluídos.
- [Personalizar](<06. GUIAS/02. POSSIBILIDADES/PERSONALIZAR.md>): voz, operação e prioridades.
- [Ferramentas e extensões](<06. GUIAS/02. POSSIBILIDADES/MODULOS-FUTUROS.md>): o que precisa de configuração adicional.
- [Instalação e atualização](<06. GUIAS/01. INSTALAÇÃO/INSTALAR.md>): alternativas e cuidados para sua cópia.

O boonOS está em beta e segue evoluindo. Teste com um projeto seu, conte pra gente como foi e, se curtir, deixe uma estrela aqui no GitHub. Para acompanhar a comunidade e saber quando a primeira turma abrir, entre na lista em [boonos.tech](https://boonos.tech).

Copyright © 2026 Studio BOON. Todos os direitos reservados. Consulte os [termos de uso](LICENSE.md).
