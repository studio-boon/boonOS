# Aprender com o trabalho

Criativo e operacional compartilham este ciclo: observar um caso, registrar a evidência, propor uma pequena mudança, aplicá-la dentro da autorização e avaliar o próximo uso. O sistema funciona por demanda, sem servidor ou agenda instalada.

Use `boon-memoria` para uma preferência ou decisão durável, `boon-melhorar-sistema` para mudar um procedimento e `boon-avaliar-skills` para comparar sua utilidade. Ao terminar uma sessão, basta identificar uma correção que vale preservar. Se não houver, não crie uma melhoria artificial.

## Evidência e maturidade

| Estado | O que comprova |
|---|---|
| Capturado | Fonte ou caso preservado, com origem e escopo |
| Proposto | Problema, destino e hipótese de mudança |
| Aplicado | Arquivo alterado e validação técnica registrada |
| Usado | Próximo trabalho real ligado à mudança |
| Avaliado | Rubrica, feedback ou resultado confronta a hipótese |
| Revertido | Mudança retirada, com motivo e histórico preservados |

Aprovação é uma decisão, não uma métrica. Uma checagem de integridade não comprova que o método melhorou. Aprendizado de cliente permanece nesse escopo até existir decisão para generalizá-lo.

## Patch pequeno com histórico

`scripts/improve.py` usa somente Python padrão. Execute a partir da raiz ou forneça `--root CAMINHO`. Ele não chama modelos, APIs, shell, Git ou agendadores. Suporta criação e substituição de pequenos arquivos UTF-8; não é ferramenta de migração, rename, remoção em massa ou edição de binários.

Prepare um JSON dentro do workspace:

```json
{
  "title": "Preservar a pergunta que faltou no briefing",
  "evidence": ["00. TRABALHO/MEU-PROJETO/feedback.md"],
  "changes": [
    {"path": "00. TRABALHO/MEU-PROJETO/checklist.md", "content": "# Checklist\n\n- Confirmar público e objetivo.\n"}
  ],
  "checks": [
    {"type": "contains", "path": "00. TRABALHO/MEU-PROJETO/checklist.md", "text": "Confirmar público e objetivo."}
  ]
}
```

O exemplo define um formato; os caminhos precisam existir no seu caso. Cada arquivo de mudança exige uma checagem: `contains`, `not_contains` (ambas com `text` não vazio) ou `json`. Comandos executáveis não são aceitos. A evidência precisa ser um arquivo local; para referência externa, preserve primeiro URL, autoria e trechos necessários em uma nota.

```sh
python3 scripts/improve.py --root . prepare --spec caminho/da-melhoria.json
python3 scripts/improve.py --root . status RUN_ID
python3 scripts/improve.py --root . apply RUN_ID --apply
python3 scripts/improve.py --root . rollback RUN_ID --apply
```

No Windows, use `python` ou `py -3` quando for o comando disponível. A preparação não muda o alvo: cria `01. SISTEMA/01. EVOLUÇÃO/RUN_ID/` com `registro.json`, diff e cópias antes/depois com SHA-256. Esse histórico local é ignorado pelo Git por padrão e pode conter conteúdo privado; é recuperação local, não backup externo nem prova de sincronização.

Revise o candidato e confirme que a autorização cobre os arquivos. `--apply` registra a execução explícita; não representa aprovação humana obtida pelo script. Autorização já concedida não precisa ser solicitada outra vez.

Antes de aplicar, o script verifica hashes dos alvos, candidatos, preimagens e fontes. Spec inválido ou drift bloqueia antes de alterar os alvos. Em falha durante a escrita, tenta restaurar apenas os arquivos que escreveu e cujos hashes ainda coincidem; conflitos ficam registrados sem sobrescrever edição posterior. A substituição de cada arquivo é atômica, mas o conjunto não é uma transação resistente a queda de energia. Após interrupção abrupta, preserve o histórico e inspecione os hashes antes de retomar; confira o processo antes de remover um lock residual.

Rollback exige estado `applied` e alvos iguais à saída aplicada. Ele restaura preimagens, remove somente arquivos criados por aquela execução e preserva diretórios. Qualquer edição posterior bloqueia a reversão para reconciliação humana. Não edite os registros ou snapshots para contornar um bloqueio.

Limites: até 20 arquivos por patch e 2 MB por arquivo; sem caminhos absolutos, `..`, symlinks/junctions, `.git` ou escrita no próprio histórico. Evite modificações concorrentes na árvore durante uma aplicação. Nenhum conteúdo de spec é interpretado como código.

## Avaliar o efeito

Após a integridade passar, rode as verificações pertinentes: para estrutura/skills, `python3 scripts/check.py --root .`; para uma alteração funcional, seu caso representativo. Use [AVALIACAO.template.md](<../05. BIBLIOTECA/03. EVOLUÇÃO/AVALIACAO.template.md>) e ligue o resultado ao `run_id`.

O campo `functional_evaluation` permanece `not_evaluated` no recibo técnico: o script não faz julgamento comportamental. Registre o caso, artefato, rubrica e decisão em nota separada, sem reescrever o recibo. Uma regressão pode levar ao rollback; falta de evidência mantém o efeito em aberto.

## Recorrência opcional

`AUTOMACOES.json` começa com `scheduler_enabled: false`; `INTEGRACOES.json` começa vazio. As skills correspondentes ajudam a configurar uma necessidade real. O núcleo não exige Discord, Drive, um fornecedor de IA ou servidor.

Uma rotina agendada deve reutilizar um comando manual testado, com leitura limitada, saída definida, timeout, lock e status por etapa. Instalação do agendador, autorização de escrita e notificações são decisões próprias; nenhuma delas acontece ao clonar ou rodar este exemplo.
