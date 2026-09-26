---
name: boon-melhorar-sistema
description: Transforma erro recorrente, feedback ou aprendizado em uma pequena mudança verificável do sistema, com evidência, comparação e reversão; também fecha sessões com melhorias candidatas.
---

# Melhorar com evidência

Comece pelo trabalho concreto que falhou ou poderia melhorar. Leia sua evidência e o procedimento afetado. Se não houve aprendizado útil, encerre com “nenhuma mudança necessária”; não crie tarefas ou skills para justificar a revisão.

Escolha o menor destino: memória local, checklist, template, skill ou script. Declare problema, hipótese, escopo e critério antes da mudança. Separe correção autorizada de proposta ainda em discussão. Permissões existentes continuam válidas; não amplie a mudança para integrações, publicação ou agendamento.

Para patches pequenos em texto UTF-8, siga [APRENDIZADO.md](<../../../01. SISTEMA/APRENDIZADO.md>): prepare um spec com evidência, candidato e checagens; rode `python3 scripts/improve.py --root . prepare --spec CAMINHO.json`. Inspecione diff e hashes. Use `apply RUN_ID --apply` somente para a alteração autorizada.

Depois, rode a verificação pertinente ao arquivo. Para skills/estrutura, `python3 scripts/check.py --root .`. Uma substring presente ou JSON válido comprova integridade, não qualidade do método. Execute um caso representativo e use rubrica ou feedback para avaliar o efeito; registre o resultado no modelo de avaliação. Sem caso, declare “aplicado, efeito não avaliado”.

Se a mudança piorar o trabalho, `rollback RUN_ID --apply` reverte apenas quando não houve edição posterior. Se detectar drift, preserve o arquivo e proponha reconciliação. Não force rollback nem descarte trabalho novo.

Saída: evidência, mudança, validação técnica, efeito observado ou pendente, `run_id` e como reverter. A rotina funciona por demanda. Agendamento é opcional e vem desligado.
