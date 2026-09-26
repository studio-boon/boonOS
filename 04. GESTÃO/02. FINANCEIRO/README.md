# Financeiro

`boon-contas` registra obrigações e movimentos; `boon-financeiro` calcula; `boon-conciliar` compara extrato; `boon-saude-operacional` interpreta riscos com projetos e capacidade.

Não existe saldo real inicial no template. Antes de criar `98. PRIVADO/livro.json`, obtenha moeda, data, saldo verificado e fonte. Valores desconhecidos são pendências, não zero.

[Contrato e CLI](<../../05. BIBLIOTECA/02. OPERACIONAL/FINANCEIRO.md>) · [Modelo de livro](<../../05. BIBLIOTECA/02. OPERACIONAL/LIVRO.template.json>) · [Exemplo com resultados verificáveis](<../../06. GUIAS/03. EXEMPLOS/OPERACAO.md>).

Relatórios gerenciais e conciliações reais ficam em `98. PRIVADO`, com corte e fonte. O script lê JSON e imprime resultado; não acessa banco nem faz transações. Um sistema financeiro já utilizado pode permanecer canônico: adapte a leitura sem criar um segundo registro conflitante.
