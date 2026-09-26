# Uma operação completa, com dados fictícios

Esta é uma demonstração local. **Nenhuma pessoa, contrato, pagamento ou fornecedor abaixo é real.** O objetivo é verificar a conexão entre capacidades sem acessar contas ou enviar mensagens.

Leia o caso com o agente ou peça: “Use este exemplo fictício para me mostrar a trilha operacional; calcule o livro no corte de 25/09/2026 e diga o que ainda falta decidir”.

## A história

Um pequeno time fictício recebeu uma oportunidade `O-001` para produzir uma apresentação. A relação é `C-001`, o projeto é `P-001` e a proposta é `PROP-001`. Esses IDs permanecem os mesmos ao longo do ciclo.

| Etapa | Ação e evidência fictícia | Saída que a skill deve produzir |
|---|---|---|
| Comercial | Conversa registrada sobre objetivo, audiência e prazo | Oportunidade com hipótese separada do pedido, estágio e próximo passo |
| Precificação | Escopo e custos foram estimados; o preço precisa de premissas | Memória de cálculo privada, sem tabela de preço imposta pelo sistema |
| Proposta | Escopo, duas parcelas totalizando 2400 e condições foram apresentados | Documento revisável; criado não significa enviado |
| Aceite e cliente | O caso informa aceite em 10/09; assinatura pode continuar pendente | Mesma relação C-001, fonte do aceite e onboarding |
| Projeto | Apresentação com narrativa, peças e revisão | P-001 único para criação e operação, critérios e próximos passos |
| Fornecedor | Serviço contratado por 700, com fonte fictícia | Obrigação a pagar e compromisso de entrega |
| Contas | Recebimento parcial e pagamento parcial com devoluções | Eventos distintos, ligados às obrigações |
| Criação e entrega | O caso simula uma entrega para revisão em 25/09 | Critérios e candidato; sem inferir aprovação ou envio |
| Fechamento | Cálculo de caixa e pendências no corte de 25/09 | Relatório derivado do livro, com vencidos e previsões separados |
| Apoio contábil | Originais fictícios são representados pelos IDs `demo:` | Índice e faltas para revisão, sem afirmar conformidade fiscal |
| Aprendizado | A devolução parcial mostrou necessidade de separar estado e atraso | Proposta de melhoria local; testar antes de torná-la regra |

Os documentos `demo:` são referências fictícias, não anexos existentes. O caso não deve ser usado como comprovante de um fato real.

## Execute o cálculo

Da raiz do repositório:

```sh
python3 scripts/finance.py "06. GUIAS/03. EXEMPLOS/operacao.json" --as-of 2026-09-25
python3 -m unittest discover -s tests -p test_finance.py -v
```

No Windows, troque `python3` por `python` quando necessário. Python deve estar instalado. Os arquivos [operacao.json](operacao.json) e [script financeiro](../../scripts/finance.py) são locais; a execução não consulta banco nem escreve no livro.

## Resultados esperados

| Medida em 25/09/2026 | Valor fictício em BRL |
|---|---:|
| Saldo inicial | 1000.00 |
| Recebimentos líquidos de devoluções | 1000.00 |
| Pagamentos líquidos de devoluções | 300.00 |
| **Caixa do livro** | **1700.00** |
| A receber comprometido | 1400.00 |
| A pagar comprometido | 500.00 |
| A receber previsto, ainda sem aceite | 900.00 |
| A pagar previsto, ainda não contratado | 200.00 |
| Parte vencida do receber comprometido | 1000.00 |
| Parte vencida do pagar comprometido | 400.00 |
| Cenário de liquidar todos os compromissos | 2600.00 |

A fórmula do caixa é `1000 + 1000 - 300 = 1700`. O cenário de compromissos é `1700 + 1400 - 500 = 2600`; não representa dinheiro disponível, não tem data de realização e não inclui as previsões.

Detalhes que evitam falsas conclusões:

- R-001 tem valor 2000, recebeu 1200 e devolveu 200: saldo pendente 1000. Está **parcial e vencida** ao mesmo tempo.
- P-001 tem valor 700, pagou 400 e recebeu devolução de 100: falta pagar 400, também vencidos.
- RC-001 recebeu 500, devolveu integralmente e foi cancelada. Os dois eventos permanecem no histórico; sua pendência é zero.
- R-002 tem recebimento em 01/10. Esse evento existe no arquivo, mas fica fora do corte de 25/09. Em 01/10, o caixa passa para 2100.
- PR-001 e PP-001 são previsões. Não entram no caixa, no saldo comprometido ou no atraso.
- Entradas/saídas brutas são 1800/1100 por incluírem as direções das devoluções. Os líquidos são 1000/300; ambos produzem o mesmo efeito de caixa, mas não são a mesma métrica.

## Experimente as fronteiras

Em uma cópia temporária do JSON, nunca no controle real:

1. Repetir E-001 com o mesmo ID deve falhar por duplicata.
2. Remover o estorno de RC-001 deve falhar: cancelar não apaga caixa recebido.
3. Tentar liquidar PR-001 deve falhar: previsão não é compromisso.
4. Trocar um valor por `null` ou por número JSON deve falhar: quantia exige string decimal explícita.
5. Alterar o corte para 17/09 mostra o adicional ainda ativo e recebido, antes do estorno/cancelamento.

Os testes automatizados verificam essas situações e conciliação, centavos, liquidação excessiva e imutabilidade do arquivo. Os testes de cálculos não provam adoção real, habilidade de um contador ou qualidade das entregas criativas.

## Conciliação e revisão contábil

O [contrato financeiro](<../../05. BIBLIOTECA/02. OPERACIONAL/FINANCEIRO.md>) traz o JSON de extrato e o comando com `--statement`. A correspondência explícita exige data, direção e valor iguais; coincidência sem vínculo é só candidata. Datas diferentes, taxas e agrupamentos ficam para revisão.

Depois do cálculo, monte um índice usando o [modelo contábil](<../../05. BIBLIOTECA/02. OPERACIONAL/CONTABILIDADE.md>): livro e corte, movimentos, cancelamento, devoluções e documentos faltantes. Este exemplo não fornece comprovantes reais nem checklist fiscal; portanto o resultado é **demonstração preparada para revisão**, nunca “contabilidade fechada”.

## Primeira missão com seus dados

Escolha um projeto ou uma semana. Traga apenas as informações necessárias, indique o que é confirmado e o que falta. O agente deve mostrar a saída útil e o próximo passo antes de ampliar a configuração. Seus documentos privados não precisam ser publicados para o sistema funcionar.
