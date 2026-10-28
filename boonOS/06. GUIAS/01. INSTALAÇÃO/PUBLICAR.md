# Publicar uma edição do template

Guia para quem mantém o pacote. Edição: **boonOS Beta**. Branch principal de distribuição: `main`. Identificador técnico desta base: `0.1.0-beta.7`. A identificação nos arquivos não prova publicação remota.

## Vitrine e pacote

No repositório público, os arquivos editáveis do sistema ficam em `boonOS/`. O README e a licença dessa pasta são as fontes; na raiz do repositório, execute `python3 .github/sync_vitrine.py` para gerar as cópias de apresentação com os links ajustados. O workflow confere essa relação com `--check` para evitar versões divergentes. Na instalação pessoal aberta diretamente como pasta de trabalho, continue usando os arquivos locais; não é preciso gerar a vitrine.

## Preparar o pacote

1. Confira versão em `boonos.json`, nomes no README, catálogo e comandos de instalação.
2. Revise fontes, licenças e atribuições. Distribua apenas materiais autorizados, com exemplos fictícios identificados. Exclua contexto pessoal, documentos de clientes, valores internos e configuração de serviços.
3. Confira links e referências depois de movimentos de pastas. Preserve o caminho de atualização da edição antiga e da beta personalizada.
4. Verifique extensões e espelhos antes de sincronizar.

Na raiz, com Python 3.10 ou superior:

~~~bash
python3 scripts/sync_skills.py --check
python3 scripts/check.py --release
git diff --check
~~~

Se os espelhos precisarem de atualização, revise primeiro o resultado de `python3 scripts/sync_skills.py`. Use `--apply` apenas quando os conflitos e o escopo estiverem resolvidos. Não apague extensões locais para fazer um check passar.

## Validar o que será anunciado

Em uma cópia isolada:

- abra como pessoa nova, inicie o onboarding, pause com checkpoint autorizado e retome em outra sessão;
- faça uma missão criativa e uma operacional com exemplos identificados;
- confira registros financeiros com cálculo reproduzível e casos de parcial, duplicata e cancelamento;
- execute uma melhoria com evidência e uma regressão que deva ser recusada;
- simule atualização preservando contexto, extensões e documentos privados.

Use [o cenário de onboarding](<../03. EXEMPLOS/ONBOARDING.md>) como material bruto de avaliação independente. Registre agente, versão, sistema operacional, comandos, saída e limitações. Um teste estrutural não substitui o uso no agente. Não anuncie compatibilidade executada em Windows/macOS ou Claude/Codex sem o registro correspondente.

## Publicar e conferir

Depois da validação e dentro da autorização de publicação:

1. Publique a alteração na branch de distribuição escolhida e confira seu commit remoto.
2. Crie a tag/release somente com a versão exata revisada e suas limitações.
3. Teste a instalação por ZIP em uma pasta vazia; confirme ausência de `.git`, `boonos.json`, catálogo e arquivos ocultos.
4. Confira os links de distribuição e, se usar “Use this template”, qual versão ele realmente entrega.
5. Compartilhe o link que aponta para essa edição. Atualizar a branch padrão é uma decisão de release distinta.

Publicação técnica não comprova aceitação por quem recebeu, configuração do agente ou funcionamento de integração. Registre esses resultados separadamente.
