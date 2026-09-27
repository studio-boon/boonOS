# Mapa das 42 skills

As duas áreas compartilham a mesma base de contexto. As descrições abaixo dizem o que cada skill recebe e produz; a maturidade e as dependências ficam no [catálogo estruturado](<../../01. SISTEMA/CATALOGO.json>). Incluída no pacote não significa testada em todos os agentes, plataformas ou situações.

Peça pelo resultado em linguagem comum. O nome serve para localizar o processo quando você quiser ser específico. A sintaxe `$nome` pode ser usada no Codex; em outro agente, peça a skill local pelo nome.

## Criativo — 14

| Skill | O que trazer | Resultado principal |
|---|---|---|
| `$copywriting` | objetivo, público e contexto | mensagem e versões revisáveis |
| `$writing-filter` | texto, intenção e voz de referência | revisão fiel e critérios de linguagem |
| `$brand-storytelling` | proposta, público e evidências | decisões de narrativa de marca |
| `$content-strategy` | objetivo, público e capacidade | prioridades e linha editorial |
| `$carrossel` | ideia, público e formato | sequência, copy e direção visual |
| `$post-social` | mensagem e canal | peça estática planejada com hierarquia |
| `$design` | briefing, referências e restrições | conceito e direção para produção |
| `$design-review` | peça e critério esperado | problemas priorizados e próxima versão |
| `$taste` | referências e contexto de uso | critérios observáveis e repertório |
| `$image-direction` | intenção, formato e referências | direção de imagem e briefing de produção |
| `$presentation` | público, objetivo e conteúdo | narrativa, sequência e plano de deck |
| `$site-design` | usuário, objetivo e conteúdo | arquitetura e direção de interface |
| `$interface-polish` | interface e comportamento esperado | ajustes de estados, detalhes e leitura |
| `$portfolio-case-study` | papel, processo e evidências | case com contribuição e resultado atribuídos |

## Operacional — 14

| Skill | O que trazer | Resultado principal |
|---|---|---|
| `$boon-projetos` | escopo, pessoas, prazo e estado | marcos, responsabilidades e impedimentos |
| `$boon-rotina` | prioridades, compromissos e capacidade | semana viável e decisões pendentes |
| `$boon-reunioes` | notas ou transcrição com origem | decisões atribuídas, tarefas e lacunas |
| `$boon-clientes` | aceite e contexto | cadastro e projeto com histórico preservado |
| `$boon-comercial` | oportunidade e evidências | qualificação, estágio e próximo passo |
| `$boon-propostas` | diagnóstico, escopo e preço | proposta local revisável |
| `$boon-precificar` | esforço, custos e premissas | cenários com cálculo reproduzível |
| `$boon-contas` | compromissos e confirmações | registro de receber/pagar e fontes |
| `$boon-financeiro` | registros e período | realizado, vencimentos e projeções |
| `$boon-conciliar` | lançamentos e extrato fornecido | correspondências candidatas e divergências |
| `$boon-contabilidade` | período, fontes e checklist acordado | índice, faltas e pacote para revisão contábil |
| `$boon-saude-operacional` | dados de caixa, margem e capacidade | riscos e decisões com premissas |
| `$boon-fornecedores` | necessidade, critérios e cotações | comparação e compromissos |
| `$boon-documentos` | fontes recebidas e versões | índice, vigência e pendências |

## Base compartilhada — 14

| Skill | O que trazer | Resultado principal |
|---|---|---|
| `$init` | situação, respostas e contexto existente | perfil, checkpoint e primeira missão |
| `$overview` | registros e prioridades | panorama com fontes e próximo passo |
| `$router` | intenção ou demanda ampla | rota pertinente e início do trabalho |
| `$grill-me` | ideia ou decisão | perguntas que resolvem pontos essenciais |
| `$study-playbook` | referência e objetivo de aprendizado | síntese atribuída e prática |
| `$skill-creator` | processo reutilizável e casos | skill ou playbook com critérios |
| `$boon-memoria` | aprendizado e origem | registro reconciliado por pessoa e escopo |
| `$atualizar` | workspace, registros e data de corte | reconciliação com fontes, conflitos e próximos ajustes |
| `$compactar-contexto` | trabalho atual, decisões, caminhos e limites | checkpoint curto para retomar em outro momento ou agente |
| `$boon-melhorar-sistema` | fricção e evidência | proposta pequena, teste e histórico |
| `$boon-avaliar-skills` | casos, versão e rubrica | comparação rastreável de comportamento |
| `$boon-gerir-skills` | catálogo, versões e extensões | manutenção com personalizações preservadas |
| `$boon-integracoes` | necessidade, serviço e escopo | configuração proposta e teste verificável |
| `$boon-automacoes` | fluxo validado e frequência | rotina especificada com executor e controle |

## Capacidade e execução

Direção visual não comprova geração de imagem; roteiro não comprova exportação de slides. O agente verifica a ferramenta disponível antes de prometer o arquivo final.

Contas registram fatos com fonte; financeiro calcula visões; conciliação compara registros; saúde operacional interpreta implicações; contabilidade organiza o conjunto documental. Pagamentos, envio de obrigações e validação oficial não são executados por uma análise local.

Integrações e automações começam sem serviços externos ativos. Uma primeira missão pode funcionar só com os arquivos trazidos pela pessoa.

`compactar-contexto` cria um registro portátil e legível. Ele não aciona nem substitui comandos ou rotinas nativas de compactação da janela de contexto do agente.

A seleção prioritária fica em `01. SISTEMA/SKILLSET.md`. Para exemplos por intenção, leia [O que dá para fazer](POSSIBILIDADES.md).
