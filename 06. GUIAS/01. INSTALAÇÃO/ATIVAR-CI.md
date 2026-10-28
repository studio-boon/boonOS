# Manter os testes automáticos no GitHub

Esta etapa é de manutenção do template. Não é necessária para instalar ou usar o boonOS.

O workflow está ativo em `.github/workflows/check.yml` no repositório de origem. As seis combinações de Linux/macOS/Windows com Python 3.10/3.13 passaram na [primeira execução completa](https://github.com/studio-boon/boonOS/actions/runs/36204735331). Os 66 testes também passaram localmente em macOS/Python 3.14.4. [check.workflow.yml](check.workflow.yml) mantém uma cópia da configuração para referência.

Se sua cópia não tiver o workflow, use estes passos com autorização para configurar CI e uma sessão/permissão apropriada:

1. Use a branch `main` ou uma branch de manutenção que contenha esta release completa.
2. Copie `check.workflow.yml` deste diretório para `.github/workflows/check.yml`, preservando o conteúdo.
3. Inclua o novo caminho e seu SHA-256 em `distribution.json`, após revisar a alteração. O manifesto é uma lista explícita de distribuição; não inclua contexto pessoal ou arquivos locais por varredura indiscriminada.
4. Confira `python3 scripts/check.py --release` e `python3 -m unittest discover -s tests -v` antes de publicar a alteração.
5. No GitHub Actions, confira o commit e os seis resultados da matriz. Registre falhas e corrija-as antes de anunciar compatibilidade executada.

O workflow usa permissões de leitura do repositório e executa somente os verificadores, exemplos e exportador do pacote. Não configura integrações, não publica releases e não usa segredos. Testes do núcleo Python não substituem um onboarding real em cada aplicativo.
