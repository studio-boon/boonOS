# Origem do pacote

Este pacote evolui o próprio repositório `tchelove/boonOS` a partir do commit
`982db2918d812adf646ac864f4e4d4d468b43d5c`. As skills existentes mantêm seus
identificadores; o catálogo indica o que foi herdado e o que entrou na versão 2.1.

Os fluxos novos foram escritos para este template a partir de requisitos de
produto. Não carregam dados de clientes, preços, percentuais, credenciais,
configurações de serviços ou cópias de skills privadas da operação de origem.

Uma coletânea herdada de citações de entrevistas, sem fonte e licença de
redistribuição documentadas no pacote, foi retirada das duas árvores de skills.
Ela não era dependência do fluxo `brand-storytelling`. O histórico Git anterior
continua sendo o registro do estado da versão antiga.

Os scripts usam apenas a biblioteca padrão do Python. Ferramentas de geração,
edição, comunicação e armazenamento externo não vêm embutidas. Cada integração
mantém seus próprios termos, requisitos e estado de conexão.

Conteúdo e personalizações de quem usa o sistema não fazem parte da release.
O exportador compara hashes com a allowlist antes de criar um pacote e recusa
arquivos do template modificados. Ele não é um backup do workspace pessoal.
