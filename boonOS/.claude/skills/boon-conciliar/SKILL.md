---
name: boon-conciliar
description: >
  Compara livro e extrato fornecidos, aponta correspondências, ambiguidades, valores divergentes e movimentos ausentes. Use para conferência de recebimentos/pagamentos; não importa banco nem baixa contas automaticamente.
---

# Conciliar

Uma coincidência de valor é candidata, não prova de correspondência.

## Fontes e entrada

Leia a seção de conciliação do [contrato financeiro](<../../../05. BIBLIOTECA/02. OPERACIONAL/FINANCEIRO.md>). Obtenha livro, extrato fornecido, moeda, intervalo e cobertura. Não acessar conta bancária por inferência. Se a fonte for CSV/PDF, preservar o original e criar JSON derivado com IDs e linhas de origem; conferir a extração antes de usar.

## Condução

1. Validar que os arquivos representam a mesma moeda, início de controle e conjunto de contas. Se isso não estiver claro, explicitar a limitação antes de chamar qualquer resultado de completo.
2. Executar `python3 scripts/finance.py LIVRO --as-of AAAA-MM-DD --statement EXTRATO`.
3. Exibir `matched`, `divergence`, `candidate`, `ambiguous`, `unmatched` e eventos do livro sem correspondência. Candidato único também exige revisão.
4. Investigar taxas, agrupamentos, datas de compensação, duplicatas ou estornos com a fonte original. Não forçar soma ou associação só para zerar diferenças.
5. Apresentar correções propostas e vínculos com evidência. Persistir mudanças somente no escopo de registro autorizado, via contrato de contas; repetir cálculo após a correção.

## Saída e conclusão

Relatório em `04. GESTÃO/02. FINANCEIRO/98. PRIVADO/CONCILIACAO-AAAA-MM-DD.md`, apontando aos arquivos e ao intervalo. Extrato fica na fonte protegida e só uma cópia derivada é mantida quando necessária.

Concluído quando cada divergência tem explicação ou pendência, e nenhum candidato foi promovido sem evidência. `complete=true` do script só cobre os arquivos fornecidos: não prova completude do extrato, autenticidade bancária ou revisão contábil. Levar faltas documentais ao pacote contábil quando pertinente.
