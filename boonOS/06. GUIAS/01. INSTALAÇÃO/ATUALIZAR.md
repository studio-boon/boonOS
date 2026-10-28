# Atualizar sem perder seu contexto

A migração cria uma instalação nova a partir desta release e da sua pasta antiga. A origem permanece intacta. Não execute `git pull` por cima do seu sistema personalizado para trocar a estrutura de pastas.

Mantenha três caminhos separados: a release nova, sua instalação antiga e um destino que ainda não existe. Use a release íntegra, com `distribution.json` e `scripts/migration-baselines.json`. O script confere a allowlist e seus hashes antes de copiar.

Na pasta da release nova, veja primeiro a prévia:

```sh
python3 scripts/migrate.py "CAMINHO/INSTALACAO-ANTIGA" "CAMINHO/INSTALACAO-NOVA"
```

No Windows, use `python` ou `py -3` se esse for o comando disponível. Mantenha aspas nos caminhos com espaços. A prévia só lê: mostra destinos, skills, exclusões e conflitos. Com o plano revisado, execute:

```sh
python3 scripts/migrate.py "CAMINHO/INSTALACAO-ANTIGA" "CAMINHO/INSTALACAO-NOVA" --apply
```

## O que é preservado

| Origem | Destino |
|---|---|
| `_00. TRABALHO/` ou `00. TRABALHO/` | `00. TRABALHO/` |
| `_01. SISTEMA/` ou `01. SISTEMA/` | `01. SISTEMA/`, preservando contexto, perfil, onboarding, skillset e decisões |
| `_02. MEMORIA/` ou `02. MEMORIA/` | `02. MEMORIA/` |
| `_03. DOCS/` ou `03. DOCS/` | `03. DOCS/` |
| `04. GESTAO/` ou `04. GESTÃO/` | `04. GESTÃO/` |
| `_99. OLD/`, `99. OLD/` ou `99. ARQUIVO/` | `99. ARQUIVO/` |
| `_PRIVADO/` ou `_privado/` | `98. PRIVADO/` no escopo correspondente |
| `CLAUDE.md` antigo, scripts/docs/templates antigos e arquivos fora dos locais conhecidos | `99. ARQUIVO/01. MIGRAÇÃO/LEGADO/` |

O perfil YAML anterior permanece com seu conteúdo original: novos campos não são inventados. O contexto antigo de `CLAUDE.md` é arquivado e recebe um ponteiro no novo `CONTEXTO.md`, para revisão. Ele não vira automaticamente regra atual. O catálogo, contratos dos agentes, infraestrutura e scripts principais vêm da release nova; o catálogo antigo é arquivado.

Git, arquivos `.env`/`.env.*`, caches e ambientes locais não são copiados. O relatório lista nomes excluídos, sem conteúdo. Documentos privados preservados continuam protegidos por padrões de nome no `.gitignore`; isso não transforma a pasta em cofre. Histórico de migração e execução também fica fora do Git por padrão.

## Skills pessoais

Uma skill idêntica à baseline conhecida de main ou beta 2.0 recebe a versão nova. Extensões pessoais são mantidas nos dois espelhos. Se ambos os espelhos antigos existem para uma skill e divergem, a migração para: primeiro decida qual conteúdo preservar.

Se uma skill foi modificada e tem o mesmo nome de uma skill da release, a prévia aponta conflito. Você pode revisar a diferença antes de migrar ou escolher conscientemente preservar sua versão:

```sh
python3 scripts/migrate.py "CAMINHO/INSTALACAO-ANTIGA" "CAMINHO/INSTALACAO-NOVA" --prefer-local-skills
python3 scripts/migrate.py "CAMINHO/INSTALACAO-ANTIGA" "CAMINHO/INSTALACAO-NOVA" --prefer-local-skills --apply
```

Essa opção substitui o pacote inteiro daquela skill nos dois espelhos pelo conteúdo pessoal; não mistura arquivos de versões diferentes. O catálogo continua descrevendo a base da release, portanto revise as diferenças do seu override no `SKILLSET.md`. A opção não ignora espelhos divergentes, colisões ou problemas de caminho.

## Conferir a instalação nova

A cópia é montada em uma pasta temporária irmã do destino. Só é promovida após validar hashes, paridade das skills e que a origem não mudou durante o processo. O destino precisa continuar ausente; repetir o comando para a mesma pasta é recusado.

Abra `99. ARQUIVO/01. MIGRAÇÃO/MANIFESTO.json` no destino: ele registra origem, mapeamentos, hashes, exclusões, skills preservadas e validação. Contém caminhos e metadados locais e deve permanecer privado. A pasta original é sua recuperação local; a operação não comprova backup externo nem sincronização.

No destino, rode:

```sh
python3 scripts/check.py --root .
python3 scripts/sync_skills.py --check
```

Revise eventuais pendências de conteúdo pessoal. Retome o onboarding para completar campos novos usando suas próprias respostas e faça uma pequena missão criativa e uma operacional. Não apague a origem até conferir o trabalho e os arquivos importantes.

Nenhuma integração é autenticada, scheduler instalado, mensagem enviada ou código da instalação antiga executado pela migração. A cópia não afirma compatibilidade funcional de scripts e extensões pessoais arquivados. Em caso de colisão, symlink/junction ou ambiguidade, resolva o item apontado e refaça a prévia com um destino novo.
