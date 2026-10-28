---
name: boon-gerir-skills
description: Revisa a composição, procedência e sincronização das skills do workspace quando há habilidade ausente, duplicada, antiga ou inadequada ao perfil.
---

# Um pacote coerente

Leia `01. SISTEMA/SKILLSET.md`, o catálogo/lock existente e os diretórios `.agents/skills` e `.claude/skills`. Separe disponibilidade, prioridade para o perfil e maturidade comprovada. Contagem de pastas não comprova ferramentas autenticadas nem qualidade.

Comece com `python3 scripts/check.py --root .` e `python3 scripts/sync_skills.py --check`. A fonte é `.agents/skills`; `.claude/skills` oferece compatibilidade. Não transforme automaticamente extras locais em erro ou sobrescreva conflitos do usuário.

Proponha adicionar/remover algo apenas para um trabalho real: gatilho, entrada, entrega, próximo passo, origem/licença e dependências. Uma lacuna pequena pode ser resolvida por checklist dentro de uma skill existente. Use o criador de skills disponível no ambiente se for necessário um pacote novo.

Depois de uma alteração autorizada na fonte, rode `python3 scripts/sync_skills.py --apply`; resolva os conflitos apontados de forma específica, preservando edições locais. Atualize catálogo/lock e prioridade do perfil pelo procedimento existente. Valide outra vez.

Não copie pacotes de cursos ou bibliotecas restritas para um repositório público sem autorização de redistribuição. Adaptadores dependentes de conta ou serviço devem declarar essa condição e oferecer caminho manual útil.

Saída: composição encontrada, diferenças, alterações autorizadas, validação e o que ainda depende de avaliação funcional por `boon-avaliar-skills`.
