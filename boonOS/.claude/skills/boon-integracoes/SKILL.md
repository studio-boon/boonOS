---
name: boon-integracoes
description: Planeja, configura ou verifica uma conexão externa solicitada, registrando finalidade, conta, permissões e teste; não conecta serviços apenas por encontrar uma referência a eles.
---

# Conectar com propósito

Comece pela tarefa que a conexão destrava. Leia `01. SISTEMA/INTEGRACOES.json` e as instruções oficiais do adaptador disponível. Confirme a conta e o escopo necessários; use a autorização existente para aquela ação. Se a ferramenta não estiver disponível, declare isso e mantenha um procedimento manual.

O registry descreve integrações; não armazena segredos. Use variáveis de ambiente ou o mecanismo de credenciais do ambiente. Não copie tokens para documentos, logs, specs ou exemplos.

Registre separadamente: descoberta, configuração, teste datado e atividade. Instalação não comprova autenticação. Um teste deve conferir a saída esperada e, para escrita autorizada, o efeito no destino e a conta correta. Se faltar permissão ou credencial, registre bloqueio sem inventar sucesso.

Documente finalidade, responsável, operações permitidas, caminho do adaptador, teste/última verificação, falhas e desconexão. Consulte [INTEGRACAO.template.md](<../../../05. BIBLIOTECA/03. EVOLUÇÃO/INTEGRACAO.template.md>) apenas para uma conexão concreta.

Saída: o que foi configurado e efetivamente testado, evidência, limites e próximo passo. Integração não cria rotina recorrente; use `boon-automacoes` se a pessoa pedir recorrência.
