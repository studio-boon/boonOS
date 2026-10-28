# Um ciclo de melhoria que você pode conferir

Este caso é fictício: um checklist de briefing omitiu o público. A hipótese é que uma pergunta explícita evita começar com essa lacuna. Os arquivos ficam nesta própria pasta de exemplo; não é aprendizado sobre seu negócio.

Na raiz do workspace, prepare:

```sh
python3 scripts/improve.py --root . prepare --spec '06. GUIAS/03. EXEMPLOS/01. MELHORIA/spec.json'
```

O resultado mostra um `run_id`. Abra o caminho `record` retornado e o `alteracoes.diff` na mesma pasta. O checklist de exemplo permanece intacto até a aplicação:

```sh
python3 scripts/improve.py --root . apply RUN_ID --apply
```

Abra `06. GUIAS/03. EXEMPLOS/01. MELHORIA/checklist.md`: a pergunta sobre público deve estar presente. Isso comprova aplicação e integridade. Para avaliar utilidade, use o checklist em um briefing fictício novo, observe se a pergunta foi respondida e compare com o procedimento anterior. Registre esse resultado pelo template de avaliação; o script não o infere.

Confira a reversão:

```sh
python3 scripts/improve.py --root . rollback RUN_ID --apply
```

O checklist volta ao texto anterior e o recibo passa a `rolled_back`. Se você editar o checklist entre aplicação e rollback, o script bloqueará a reversão para preservar sua edição. Restaure manualmente somente se souber o que está preservando; nunca altere hashes do recibo para forçar.

Se preparar novamente enquanto o checklist já contém exatamente o candidato, o estado será `noop`: há registro da tentativa, sem mudança do alvo. Você pode apagar o histórico somente depois de decidir que não precisa mais dele; o exemplo não faz limpeza automática.

No PowerShell, aspas simples também preservam espaços; use `python` ou `py -3` no lugar de `python3` se necessário. O script não depende de ferramentas externas, não envia mensagens e não cria agendamento.
