---
name: boon-avaliar-skills
description: Compara uma skill nova ou alterada com uma referência usando casos reais e critérios definidos antes da execução, para decidir manter, revisar ou retirar.
---

# Avaliar utilidade, não obediência ao formato

Identifique a versão alvo e a comparação: versão anterior, agente sem skill ou procedimento atual. Registre os arquivos/hashes para manter a comparação reproduzível. Não altere a skill durante a medição.

Selecione de dois a cinco pedidos realistas, incluindo um caso limite. Defina antes a rubrica apropriada: gatilho, uso das fontes, qualidade da entrega, preservação de limites e retrabalho. Se a dúvida for acionamento, inclua pedidos que não deveriam disparar a skill.

Mantenha entrada e condições comparáveis. Rode as variantes em trabalho isolado, sem tocar entregas reais nem acionar serviços pagos ou externos fora da autorização. Um revisor independente ajuda quando o julgamento é subjetivo ou o risco justifica.

Registre outputs e observações; tempo, custo e tokens só entram quando medidos. Validação do frontmatter é instalação, não desempenho. Compare a qualidade com o critério anunciado, inclusive regressões e ausência de ganho.

Use [AVALIACAO.template.md](<../../../05. BIBLIOTECA/03. EVOLUÇÃO/AVALIACAO.template.md>). Veredito: manter, revisar, dividir, juntar ou retirar; uma habilidade disponível pode continuar experimental. Mudanças decorrentes seguem `boon-melhorar-sistema`; composição e espelhos seguem `boon-gerir-skills`.

Saída: casos, baseline, evidências, ganho ou regressão, limitações e decisão. Nunca declare validação comportamental a partir de uma checagem de texto.
