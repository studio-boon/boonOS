---
name: init
description: >
  Configura ou retoma o contexto pessoal e operacional do boonOS por uma conversa
  progressiva. Use ao instalar, pedir configuração, revisar o perfil ou retomar
  um onboarding. Conecta a entrevista a uma primeira missão criativa ou operacional.
---

# init — um sistema que entende como você trabalha

## Comece pelo que já existe

Leia `AGENTS.md`, `01. SISTEMA/CONTEXTO.md`, `PERFIL.yaml`, `SKILLSET.md` e `ONBOARDING.md`. Os últimos quatro estão em `01. SISTEMA`. Leia o banco de perguntas em `05. BIBLIOTECA/03. EVOLUÇÃO/01. ONBOARDING/PERGUNTAS.md` conforme o módulo necessário.

- Perfil existente: preserve informações e autorizações. Retome pelo checkpoint ou revise o trecho solicitado.
- Instalação vazia: explique que o sistema ajuda tanto na criação quanto na operação e ofereça dois ritmos: primeira missão ou configuração aprofundada.
- Pedido concreto com informações suficientes: comece o trabalho e registre as lacunas para depois. Não obrigue a pessoa a concluir a entrevista inteira.
- Não explore contas, pastas pessoais ou fontes externas apenas porque foram mencionadas. Registre a localização; leia quando o pedido e a autorização cobrirem a fonte.

## Conduza a descoberta

Pergunte em blocos de **até três perguntas**, espere a resposta e use-a para escolher o próximo bloco. Evite várias subperguntas escondidas numa só. A cada bloco, resuma o que mudou no entendimento e aprofunde uma decisão relevante.

Prefira episódios e evidências: “qual foi o último trabalho que atrasou?” revela mais que “você é organizado?”. Não transforme a entrevista em avaliação da pessoa. Se não souber responder, proponha um exemplo ou deixe a lacuna explícita.

| Módulo | O que descobrir |
|---|---|
| Identidade | atividade, papel, solo/time, nome do sistema e idioma/fuso quando relevantes |
| Direção | atrito concreto, objetivo, prioridade e o que precisa mudar |
| Criativo | público, formatos, referências comentadas, voz e critérios de aprovação |
| Operacional | oferta, entrada do trabalho, etapas, responsáveis, capacidade, recebimentos e documentos |
| Fontes e ferramentas | onde vivem registros, qual fonte prevalece e ferramentas que quer manter |
| Permissões | contexto que pode ser salvo, acesso, ações autorizadas e limites |
| Primeira missão | material disponível, saída útil e critério observável de conclusão |

O ritmo rápido coleta o mínimo para uma missão e deixa módulos pendentes. O aprofundado percorre os módulos pertinentes, sem exigir valores financeiros ou dados de clientes desnecessários. Uma pessoa pode criar e operar; não force uma persona exclusiva.

## Mostre possibilidades durante a conversa

Depois de entender a atividade e uma dificuldade, apresente poucas possibilidades relacionadas às respostas, cobrindo as duas áreas. Use “você traz → construímos → você confere”. Exemplos completos estão em `06. GUIAS/02. POSSIBILIDADES/POSSIBILIDADES.md`.

Uma pessoa que vende serviços pode organizar uma proposta e um projeto, melhorar como apresenta o trabalho ou revisar entradas e saídas. Explique o resultado antes do nome da skill. Escolha uma missão prioritária; as outras viram possibilidades para depois.

Diferencie o que pode ser feito com arquivos e conversa do que depende de ferramenta ou integração. Um pedido de imagem não prova que há gerador de imagens. Exemplo fictício fica identificado e não alimenta contexto real, clientes ou lançamentos.

## Sintetize e salve no escopo autorizado

Antes do primeiro registro, mostre uma síntese curta com:

- pessoa/time, propósito, prioridades e contexto criativo/operacional confirmado;
- fontes de verdade, limites e ações autorizadas;
- capacidades prioritárias com motivo;
- primeira missão, critério de sucesso e lacunas;
- arquivos que serão criados ou atualizados.

Se a pessoa já autorizou salvar a configuração ou checkpoints revisados, prossiga nesse escopo. Não peça um novo “sim” a cada arquivo ou módulo. Se essa autorização ainda não existe, peça uma confirmação específica sobre o resumo e sua gravação. Uma resposta vaga não autoriza persistência.

Use `05. BIBLIOTECA/03. EVOLUÇÃO/01. ONBOARDING/PERFIL.template.yaml` como referência de estrutura. Em perfil existente, acrescente apenas o necessário; não sobrescreva campos customizados. Dados desconhecidos ficam `null` ou em listas vazias, acompanhados de lacunas quando relevante.

Atualize:

- `01. SISTEMA/CONTEXTO.md`: entendimento humano, sem entrevista bruta.
- `01. SISTEMA/PERFIL.yaml`: campos confirmados, permissões e estado.
- `01. SISTEMA/SKILLSET.md`: prioridades reais e próximos usos.
- `01. SISTEMA/ONBOARDING.md`: data, módulos, lacunas, próxima pergunta e primeira missão.
- `02. MEMORIA/voz-e-estilo.md`: somente se houver exemplos ou preferências atribuídas suficientes.

Indique origem e escopo das autorizações, sem registrar segredos ou copiar conteúdo confidencial. Ter um repositório privado não autoriza armazenar tudo.

## Pausa e retomada

Quando a pessoa pausar, ofereça ou salve um checkpoint parcial conforme a autorização já recebida. Registre contexto confirmado, módulo atual, pendências, próxima pergunta e o que foi salvo. Marque `paused`; não marque a entrevista completa por conveniência.

Sem autorização de persistência, entregue o resumo na conversa e explique que outra sessão precisará dele. Não prometa lembrar algo que não foi gravado.

Na retomada, leia o checkpoint e continue pelo que falta, aproveitando respostas já dadas. Se o usuário corrigir um fato, atualize o trecho correspondente no escopo autorizado e preserve o histórico de decisões relevantes.

Estados: `not_started`, `in_progress`, `paused` e `active`. `active` indica contexto suficiente para trabalhar, mesmo com módulos pendentes. Preencha `completed_modules`, `pending_modules`, `unknowns`, `next_question` e a missão de modo coerente.

## Faça a primeira missão

Depois da síntese, use a skill pertinente e conclua uma saída útil com o material disponível. Se faltar algo que realmente impede a execução, peça somente esse dado. Se a pessoa quiser apenas configurar, registre a missão sem executá-la.

No fechamento, mostre resultado, evidência de verificação, o que foi salvo, o que continua aberto e uma próxima ação. Para voltar ao contexto, a pessoa pode dizer “me situa”. Não transforme o fim da entrevista numa lista de comandos para ela executar.
