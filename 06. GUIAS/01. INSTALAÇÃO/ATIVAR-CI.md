# Ativar os testes automáticos no GitHub

Esta etapa é de manutenção do template. Não é necessária para instalar ou usar o boonOS.

Os 66 testes desta release foram executados localmente em macOS com Python 3.14.4. A matriz remota de Linux/macOS/Windows e Python 3.10/3.13 está preparada em [check.workflow.yml](check.workflow.yml), mas não está ativa. A credencial usada na publicação não autoriza criar arquivos de workflow.

Com autorização para configurar CI no repositório e uma sessão/permissão apropriada:

1. Use a branch `beta/2.1` ou uma branch de manutenção que contenha esta release completa.
2. Copie `check.workflow.yml` deste diretório para `.github/workflows/check.yml`, preservando o conteúdo.
3. Inclua o novo caminho e seu SHA-256 em `distribution.json`, após revisar a alteração. O manifesto é uma lista explícita de distribuição; não inclua contexto pessoal ou arquivos locais por varredura indiscriminada.
4. Confira `python3 scripts/check.py --release` e `python3 -m unittest discover -s tests -v` antes de publicar a alteração.
5. No GitHub Actions, confira o commit e os seis resultados da matriz. Registre falhas e corrija-as antes de anunciar compatibilidade executada.

O workflow usa permissões de leitura do repositório e executa somente os verificadores, exemplos e exportador do pacote. Não configura integrações, não publica releases e não usa segredos. Testes do núcleo Python não substituem um onboarding real em cada aplicativo.
