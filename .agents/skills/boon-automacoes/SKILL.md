---
name: boon-automacoes
description: Desenha e testa rotinas recorrentes solicitadas depois de um fluxo manual funcionar, com limite de execução, verificação, falha contida e opção de desligar.
---

# Automatizar um processo que já funciona

Leia `01. SISTEMA/AUTOMACOES.json`. Identifique entrada, saída verificável e quem responde pela rotina. Se ainda não existe execução manual confiável, produza primeiro esse caso e registre a lacuna; um cron não corrige um processo indefinido.

Defina trigger, escopo, permissões, custo/tempo máximo, lock contra sobreposição, timeout, retries limitados, deduplicação, logs e critério de parada. Distingua execução, validação da saída e efeito externo. Falha de etapa obrigatória torna o resultado parcial ou falho.

Use [AUTOMACAO.template.md](<../../../05. BIBLIOTECA/03. EVOLUÇÃO/AUTOMACAO.template.md>). Teste manualmente sucesso, repetição e falha, sem mensagens ou mutações externas fora da autorização. O mesmo comando deve ser útil sem scheduler.

O pacote vem sem agendador instalado. Ativar recorrência requer o pedido correspondente e configuração real do ambiente: cron, launchd, Task Scheduler ou serviço escolhido. Mantenha um único disparador e documente como pausar/remover. Não instale todos os adaptadores por conveniência.

Registre configuração e evidência da execução efetiva separadamente. A primeira execução manual não comprova que o horário programado funciona. Marque ativo somente após verificar o disparo real; até lá, use configurado ou em teste.

Saída: fluxo manual, teste, estado do agendamento, logs, comportamento em falha e comando de desligamento. O autoaprimoramento padrão continua por demanda.
