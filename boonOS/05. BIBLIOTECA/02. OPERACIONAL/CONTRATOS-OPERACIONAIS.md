# Contratos compartilhados

As áreas Criativo e Operacional trabalham sobre o mesmo projeto. Uma área consulta a outra por identificador e fonte; não se cria um segundo projeto para representar o financeiro ou o design.

## Identidade e estado

| Registro | Identificador sugerido | Fonte canônica |
|---|---|---|
| Relação comercial | C-001 | cadastro em Gestão/Comercial |
| Oportunidade | O-001 | pipeline em Gestão/Comercial |
| Projeto | P-001 | PROJETO.md da pasta de trabalho |
| Proposta | PROP-001 | documento de escopo e condições |
| Entrega | ETR-001 | registro no projeto e arquivo da entrega |
| Documento | DOC-001 | índice documental, sem duplicar o original |
| Obrigação financeira | R-001 ou PG-001 | livro.json |
| Movimento financeiro | MOV-001 | evento imutável no livro.json |

Os códigos são sugestões. Preserve IDs que já existam; não gere outro ID porque a pasta mudou de lugar ou o prospect virou cliente. Cada tipo tem seu próprio espaço de IDs.

Um registro durável informa fonte, data, responsável quando conhecido e status. Use `não confirmado` para uma lacuna; não converta silêncio em aceite, ausência de arquivo em inadimplência ou data de modificação em progresso.

## Passagens verificáveis

- **Oportunidade → proposta:** necessidade, decisor quando conhecido, escopo e próximo passo. Estimativa não é receita.
- **Proposta → cliente:** aceite atribuído e sua fonte. Contrato assinado, pagamento e onboarding têm estados separados.
- **Cliente → projeto:** objetivo, entregas, limites, responsável, marcos e critérios de aceitação. Campos desconhecidos geram pendências concretas.
- **Projeto → criação:** público, intenção, restrições, copy/fonte aprovada e critérios. A decisão visual volta ao mesmo projeto.
- **Projeto → financeiro:** obrigação e moeda documentadas; recebimento só com evidência ou confirmação explícita atribuída. Custos previstos continuam previstos.
- **Entrega → fechamento:** aprovação, entrega/envio, recebimento pelo destinatário e pagamento são verificações distintas.
- **Fechamento → memória:** problema, evidência, aprendizado e aplicação possível. Uma hipótese não altera regra global automaticamente.

## Onde guardar

Projeto: `00. TRABALHO/NN. NOME/PROJETO.md`. Quando uma entrega pedir etapas, use `01. FONTES`, `02. PRODUÇÃO`, `03. APROVAÇÃO` e `00. PRONTOS` dentro de sua pasta numerada. Criar apenas as etapas necessárias.

Registros da operação: `04. GESTÃO/`. Dados financeiros e comerciais reais ficam em `98. PRIVADO` ou na fonte externa autorizada, com índice mínimo. A pasta é organização; permissões e exclusão de versionamento precisam estar configuradas. Documentos fiscais e dados pessoais completos não entram no pacote distribuído.

Não duplicar o livro em cada projeto. O plano guarda IDs das obrigações e links; o livro é a fonte dos valores. Uma proposta externa não expõe a planilha interna de custo ou margem.

## Rotina curta

Ao terminar: qual resultado foi verificado, o que ainda depende de alguém e qual a próxima ação? Guarde o suficiente para outra sessão retomar. Só propor nova regra quando houver uma fricção concreta e critério para avaliar a mudança.
