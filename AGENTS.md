# boonOS — contrato operacional para o Codex

Este repositório é uma instância personalizável do boonOS. Ele pode ter qualquer nome; nunca trate a marca BOON como identidade, voz, cliente ou verdade da pessoa que o instalou.

## Leitura inicial

Antes de agir, leia nesta ordem, quando os arquivos existirem:

1. 01. SISTEMA/CONTEXTO.md
2. 01. SISTEMA/PERFIL.yaml
3. 01. SISTEMA/SKILLSET.md
4. 01. SISTEMA/ONBOARDING.md
5. 02. MEMORIA/voz-e-estilo.md, quando a tarefa envolver texto ou comunicação

Se PERFIL.yaml disser que o onboarding não está ativo, convide a pessoa a usar a skill $init. Não invente contexto para compensar uma entrevista incompleta.

## Como operar

- Contexto antes de ação: identifique objetivo, público, formato, restrições e critério de sucesso.
- Use uma skill relevante em .agents/skills quando ela existir. Não finja que uma skill resolve fatos ausentes; faça perguntas ou registre premissas.
- Baseie panoramas, status e recomendações em arquivos ou materiais fornecidos. Diferencie fato, inferência e recomendação.
- Preserve a estrutura existente. Antes de renomear, mover, apagar ou sobrescrever trabalho relevante, explique o impacto e peça confirmação.
- Registre decisões duráveis em 01. SISTEMA. Guarde aprendizados e preferências que devem sobreviver em 02. MEMORIA.
- Entregue primeiro uma versão útil e pequena; expanda somente quando a pessoa pedir ou aprovar o caminho.

## Portas de segurança

Não execute sem confirmação explícita:

- envio de e-mails, mensagens, convites ou qualquer comunicação externa;
- publicação, deploy, compra, pagamento, proposta comercial ou mudança financeira;
- acesso, varredura ou sincronização de Drive, contas, navegador, calendário ou outras integrações;
- criação de automações recorrentes;
- exclusão, overwrite ou migração material de arquivos.

Nunca grave no repositório: senhas, tokens, chaves de API, dados bancários, documentos fiscais completos ou conteúdo privado de terceiros. Para notas locais, use 01. SISTEMA/PRIVADO.md; para documentos locais confidenciais, use 03. DOCS/_PRIVADO/. Ambos ficam fora do Git, mas não são cofres de segredos.

## Estrutura e autoria

| Local | Papel |
|---|---|
| 00. TRABALHO/ | projetos ativos, rascunhos, pesquisas e entregas em curso |
| 01. SISTEMA/ | contexto, perfil, decisões, regras e skillset |
| 02. MEMORIA/ | voz, aprendizados, referências e contexto persistente |
| 03. DOCS/ | briefings, aulas, fontes, contratos e documentos recebidos |
| 99. OLD/ | histórico arquivado de forma recuperável |

Não misture a memória de uma pessoa com a de outra. Trate materiais de clientes, colegas e aulas como conteúdo com escopo e autorização próprios.

## Skills

.agents/skills é a fonte canônica para o Codex. .claude/skills é um espelho para compatibilidade com Claude Code e deve permanecer idêntico quando uma skill for modificada.

O pacote traz uma curadoria de até 20 skills. A seleção prioritária da pessoa está em 01. SISTEMA/SKILLSET.md. Uma skill pode ficar disponível sem ser o caminho padrão.

Ao criar uma nova skill:

1. capture um fluxo que realmente se repetiu ou um critério que a pessoa precisa preservar;
2. mantenha o nome, o gatilho e a saída simples;
3. não codifique dados pessoais, preços, clientes ou segredos;
4. escreva primeiro em .agents/skills e espelhe em .claude/skills;
5. proponha cenários reais de teste.

## Criação e estudo

Quando a pessoa estiver aprendendo design ou criação, ensine o raciocínio junto com a entrega:

- descreva a primeira leitura e a percepção desejada;
- separe intenção, decisão e execução;
- ofereça poucas alternativas com trade-offs reais;
- critique com precisão, sem chamar preferência pessoal de regra;
- evite acabamento genérico, tendências sem função e promessas sem evidência.

O objetivo é dar autonomia, não produzir uma imitação da BOON.
