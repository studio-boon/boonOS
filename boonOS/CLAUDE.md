# boonOS Beta — entrada para Claude Code

Leia e siga `AGENTS.md`, o contrato comum de trabalho deste sistema. Depois leia os arquivos de contexto ali indicados: `CONTEXTO.md`, `PERFIL.yaml`, `SKILLSET.md` e `ONBOARDING.md` em `01. SISTEMA`, e voz e estilo quando pertinente.

Antes de responder, aplique a ordem de idioma de `AGENTS.md`: escolha explícita na conversa atual, preferência autorizada em `system.locale` e, na ausência de ambas, português brasileiro. “Continue” ou “Retome” não muda o idioma por si só. Mantenha toda a resposta no idioma escolhido, mesmo quando as instruções internas estiverem em português.

Uma skill é um conjunto reutilizável de instruções, não é um comando; a pessoa pode pedir em linguagem comum. Por exemplo, uma skill de apresentação orienta organizar roteiro e slides; a execução depende das ferramentas disponíveis.

As skills locais estão em `.claude/skills`, espelho de `.agents/skills`. Para configurar ou retomar, use a skill local `init`; o pedido “use a skill local init” identifica o fluxo sem depender da interpretação de `/init` pelo aplicativo.

O contexto da pessoa vive nos arquivos de `01. SISTEMA`, não neste contrato. Preserve personalizações e autorizações vigentes. Onboarding incompleto não bloqueia uma missão que já tenha contexto suficiente.

Quando pedirem uma explicação usando o projeto da pessoa, leia primeiro `01. SISTEMA/ONBOARDING.md` e `01. SISTEMA/CONTINUIDADE.md`, consulte `06. GUIAS/02. POSSIBILIDADES/GLOSSARIO.md` e, antes de atribuir uma função a uma skill, leia seu `.claude/skills/<nome>/SKILL.md`. Se não achar contexto, declare o exemplo hipotético.
