---
name: boon-contas
description: >
  Registra obrigações a receber/pagar e movimentações confirmadas em livro JSON, preservando previsão, compromisso, liquidação parcial, estorno e cancelamento. Use para registrar ou corrigir conta; para calcular panorama use boon-financeiro.
---

# Contas

Mantenha um livro gerencial confiável. Esta skill registra o que foi combinado ou confirmado; não movimenta dinheiro.

## Contrato e entrada

Leia o [contrato financeiro](<../../../05. BIBLIOTECA/02. OPERACIONAL/FINANCEIRO.md>) antes de escrever. Use [livro vazio](<../../../05. BIBLIOTECA/02. OPERACIONAL/LIVRO.template.json>) somente após obter data, moeda, saldo inicial verificado e fonte. O exemplo público nunca vira saldo real.

Para uma obrigação, obter valor, moeda, natureza, emissão, vencimento e fonte; para compromisso, data e evidência. Para recebimento/pagamento, obter transação estável, data, valor, obrigação e comprovação ou confirmação explícita atribuída.

## Registro

1. Ler o livro existente e verificar ID/fonte antes de inserir. Mesma importação com mesmo ID não deve virar outra transação; IDs diferentes ainda exigem comparação de origem.
2. Distinguir previsão e compromisso. Um documento criado ou cobrança enviada não prova recebimento. Falta de valor ou data vira pendência fora do livro, sem zero fictício.
3. Preparar alteração no escopo solicitado, preservando preimagem e diferença. Evento confirmado não é apagado para ajustar saldo. Estorno referencia a liquidação; cancelamento com dinheiro líquido requer resolver o fluxo real conforme o contrato.
4. Validar o candidato pelo script: `python3 scripts/finance.py CAMINHO --as-of AAAA-MM-DD`. O script apenas lê. Corrigir erros com as fontes, sem mudar o fato para satisfazer o schema.
5. Persistir o registro autorizado e verificar novamente. Mostrar IDs inseridos/corrigidos, origem, efeito calculado e qualquer pendência. Se houver conflito com outra edição, reler antes de salvar.

## Saída e conclusão

Fonte padrão: `04. GESTÃO/02. FINANCEIRO/98. PRIVADO/livro.json`; se a pessoa já tem um sistema canônico, respeitar esse sistema e não criar livro paralelo sem necessidade. Registros privados não entram na versão distribuída.

Concluído quando alteração e fonte são rastreáveis, não há duplicata conhecida e validação passa. `boon-financeiro` lê o livro; `boon-conciliar` cruza extrato. O registro não confirma pagamento bancário além da evidência trazida.
