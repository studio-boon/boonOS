# Sistema

O contexto da pessoa e a forma de trabalhar ficam aqui. As entregas dos projetos ficam em `00. TRABALHO`.

| Arquivo | Responsabilidade |
|---|---|
| [CONTEXTO.md](CONTEXTO.md) | leitura humana de identidade, prioridades, criação e operação |
| [PERFIL.yaml](PERFIL.yaml) | dados estruturados confirmados, campos desconhecidos e permissões |
| [ONBOARDING.md](ONBOARDING.md) | checkpoint, módulos pendentes e primeira missão |
| [CONTINUIDADE.md](CONTINUIDADE.md) | checkpoint curto para pausa, troca de chat e retomada |
| [SKILLSET.md](SKILLSET.md) | capacidades prioritárias e próximos usos |
| [DECISOES.md](DECISOES.md) | decisões duráveis com origem e condição de revisão |
| [CATALOGO.json](CATALOGO.json) | capacidades distribuídas, dependências e maturidade |

O init mostra uma síntese antes do primeiro registro e trabalha dentro da autorização para salvar ou atualizar contexto. Preserve campos e personalizações que já existem. Arquivos narrativos explicam; dados estruturados permitem verificar; resultados de execução comprovam funcionamento.

## Pedidos do dia a dia

Você pode conversar normalmente com o agente. Por exemplo:

| Você diz | O que o agente procura fazer |
|---|---|
| “Guarda essa preferência para os próximos trabalhos.” | Registra o aprendizado autorizado na [memória](<../02. MEMORIA/README.md>), com sua origem e escopo. |
| “Salva onde paramos para eu continuar depois.” | Registra um resumo de retomada em `CONTINUIDADE.md`, com fontes, decisões e próximo passo. |
| “Retoma meu trabalho.” | Consulta o resumo salvo e as fontes pertinentes, preservando o estado e as escolhas já feitas. |
| “Confere se o contexto deste projeto está atualizado.” | Compara registros com as fontes atuais e apresenta lacunas ou conflitos. |

Para guardar ou retomar, o agente precisa ter acesso à mesma pasta. Os registros são feitos dentro da autorização dada; uma conversa sem resumo salvo não garante continuidade em outra sessão.

Por trás desses pedidos, `atualizar` reconcilia o conteúdo da instalação com as fontes atuais, e `compactar-contexto` deixa um checkpoint legível antes de pausar ou trocar de chat. Esse registro local não substitui a compactação interna de contexto oferecida por alguns agentes.

Se quiser instalar uma edição nova do boonOS, siga [Atualizar sem perder seu contexto](<../06. GUIAS/01. INSTALAÇÃO/ATUALIZAR.md>). Essa migração é diferente de revisar o contexto salvo na instalação que você já usa.

`PRIVADO.md` é uma opção para notas locais mínimas quando seu ignore tiver sido confirmado. Não use arquivos versionados para dados bancários, credenciais ou documentos confidenciais completos.
