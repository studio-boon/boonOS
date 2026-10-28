# Origem do pacote

Este pacote evolui o próprio repositório `tchelove/boonOS` a partir do commit
`982db2918d812adf646ac864f4e4d4d468b43d5c`. As skills existentes mantêm seus
identificadores; o catálogo indica o que foi herdado e o que entrou na versão 2.1.

Os fluxos novos foram escritos para este template a partir de requisitos de
produto. Não carregam dados de clientes, preços, percentuais, credenciais,
configurações de serviços ou cópias de skills privadas da operação de origem.

Uma coletânea herdada de citações de entrevistas foi retirada das duas árvores
de skills do pacote atual. Ela não era dependência do fluxo `brand-storytelling`.
O histórico Git continua acessível. A comparação de 28/10/2026 identificou
correspondência extensa, com cortes e adaptações, com o arquivo
[guest-insights de Refound AI](https://github.com/RefoundAI/lenny-skills/blob/0123453c617e1114d3097380feffb09761ce824a/skills/brand-storytelling/references/guest-insights.md).
A licença declarada para esse projeto, com seu aviso de copyright, está em
[TERCEIROS.md](<06. GUIAS/04. HISTÓRICO E TRANSPARÊNCIA/TERCEIROS.md>). Isso não comprova direitos sobre as entrevistas
citadas no material histórico; sua situação permanece em verificação.

Os scripts usam apenas a biblioteca padrão do Python. Ferramentas de geração,
edição, comunicação e armazenamento externo não vêm embutidas. Cada integração
mantém seus próprios termos, requisitos e estado de conexão.

Conteúdo e personalizações de quem usa o sistema não fazem parte da release.
O exportador compara hashes com a allowlist antes de criar um pacote e recusa
arquivos do template modificados. Ele não é um backup do workspace pessoal.
