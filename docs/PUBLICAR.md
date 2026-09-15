# Publicar uma nova versão do template

Este guia é para quem mantém o repositório-base, não para quem instalou uma cópia.

## Antes de enviar

1. confira que não há clientes, nomes pessoais, caminhos locais, preços, tokens, materiais privados ou referências internas no diff;
2. rode:

~~~bash
./scripts/check-skills.sh
git diff --check
~~~

3. abra README.md e 00. COMECE-AQUI.md como se fosse uma pessoa que nunca viu o sistema;
4. em uma pasta de teste, clone a versão final, abra no Codex e confirme que a primeira mensagem “me guia na instalação” encontra o $init;
5. confirme que 01. SISTEMA começa com placeholders e não com contexto de quem manteve o template.

## No GitHub

Depois de publicar a versão revisada:

1. deixe a branch padrão como main;
2. em Settings → General, ative Template repository se quiser oferecer o botão Use this template;
3. escolha visibilidade de acordo com os materiais que o repositório realmente contém;
4. compartilhe acesso com pessoas específicas somente depois de revisar o conteúdo e a visibilidade.

Ativar o template não concede acesso a ninguém e não transforma uma cópia em um repositório seguro por si só. A pessoa que instala continua responsável por usar uma cópia privada quando houver contexto sensível.
