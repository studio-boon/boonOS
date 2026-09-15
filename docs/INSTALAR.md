# Instalar e abrir no Codex

## Codex Desktop

1. Se o repositório estiver marcado como template no GitHub, crie um repositório seu usando Use this template; caso contrário, clone este repositório.
2. Abra a pasta local no Codex Desktop.
3. Confirme que AGENTS.md aparece na raiz do workspace.
4. Na primeira conversa, escreva $init.

## Codex CLI

~~~bash
git clone https://github.com/tchelove/boonOS.git meu-sistema
cd meu-sistema
codex
~~~

Na sessão, escreva $init ou peça: “use a skill init e configure meu sistema”.

Não há um formulário, script de configuração ou arquivo técnico para preencher antes disso. O Codex lê AGENTS.md e a skill init conduz a conversa.

Se a skill não aparecer, confirme que o arquivo .agents/skills/init/SKILL.md existe e reinicie a sessão dentro da pasta do repositório.

## Claude Code, como alternativa

Abra a mesma pasta no Claude Code e use /init. CLAUDE.md encaminha para o mesmo contexto, e .claude/skills é mantido como espelho das skills do Codex.

## Privacidade antes do primeiro commit

Use um repositório privado se for guardar clientes, contratos, notas de aula não públicas, financeiro ou qualquer informação pessoal. Para documentos locais confidenciais, use 03. DOCS/_PRIVADO/; ele não entra no Git. Revise sempre 01. SISTEMA, 02. MEMORIA e 03. DOCS antes de enviar mudanças ao GitHub.
