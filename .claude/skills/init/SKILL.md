---
name: init
description: >
  Conduz a instalação guiada do boonOS no Codex: entrevista a pessoa em blocos
  curtos, cria um contexto próprio e recomenda uma trilha de skills. Use quando
  ela disser "$init", "configura meu sistema", "começa o onboarding", "acabei de
  clonar", "me guia na instalação" ou quando o onboarding ainda não estiver ativo.
---

# init — transforme o template em um sistema seu

## O resultado

Ao final, esta pessoa terá:

- um nome próprio para o sistema;
- contexto humano em 01. SISTEMA/CONTEXTO.md;
- preferências seguras em 01. SISTEMA/PERFIL.yaml;
- um skillset prioritário em 01. SISTEMA/SKILLSET.md;
- uma primeira missão pequena e real;
- clareza sobre como continuar usando o sistema.

O template se adapta à pessoa. Não tente transformá-la em uma versão da BOON.

## Regras não negociáveis

- Faça perguntas em blocos de no máximo três por vez. Espere as respostas.
- Diga brevemente por que uma pergunta importa quando isso ajudar.
- Permita “pular por enquanto” e retome depois, sem reiniciar a entrevista.
- Não vasculhe Drive, Desktop, contas, e-mails ou documentos por iniciativa própria.
- Não peça nem grave senha, token, dado bancário, documento fiscal ou informação privada de terceiros.
- Não escreva ou substitua arquivos de contexto antes de apresentar um resumo e receber um “sim” explícito.
- Se o onboarding já estiver ativo, pergunte se a pessoa quer revisar uma parte, retomar uma entrevista pausada ou apenas começar uma missão.

## 0. Preflight

Leia, se existirem:

1. AGENTS.md
2. 01. SISTEMA/CONTEXTO.md
3. 01. SISTEMA/PERFIL.yaml
4. 01. SISTEMA/SKILLSET.md
5. 01. SISTEMA/ONBOARDING.md
6. templates/onboarding/PERGUNTAS.md

Se o status for not_started, explique em uma frase:

> Em poucos minutos vamos dar um nome ao seu sistema, escolher o que ele deve ajudar a fazer e montar uma primeira missão. Nada será salvo sem sua revisão.

## 1. Identidade

Pergunte em um bloco:

1. Como você quer chamar este sistema?
2. Como prefere ser chamado e em que idioma/fuso costuma trabalhar?
3. Você trabalha sozinho ou com um time?

Resuma o que entendeu antes de avançar.

## 2. Momento e prioridade

Pergunte:

1. O que você mais quer criar, aprender ou organizar agora?
2. Qual é o principal caos ou fricção que vale resolver primeiro?
3. O que precisa estar diferente em cerca de 90 dias?

Procure uma primeira vitória concreta, não uma lista de desejos.

## 3. Como a pessoa trabalha

Pergunte:

1. Onde ficam hoje as fontes que ela considera verdadeiras?
2. Como ela diferencia rascunho, aprovado e entregue?
3. Que ações sempre precisam de aprovação humana?

Se ela não souber, proponha defaults seguros: nada externo é enviado/publicado, documentos sensíveis ficam fora do Git e decisões importantes são registradas.

## 4. Criação e estudo

Apresente estas trilhas em linguagem simples e peça a mais próxima:

| Trilha | Ajuda principal |
|---|---|
| Criador em estudo | aprender repertório, criar peças e entender decisões |
| Designer digital | trabalhar site, interface, revisão e portfolio |
| Comunicação e marca | criar narrativa, texto, conteúdo e peças sociais |
| Autor independente | combinar as três para um projeto próprio |

Depois pergunte:

1. Quais formatos ela quer praticar primeiro?
2. Quais referências, gostos ou coisas que ela quer evitar já consegue nomear?
3. Qual missão pequena pode ser feita esta semana?

Recomende no máximo seis skills além da base. Todas as 20 continuam disponíveis, mas não trate todas como urgentes.

## 5. Privacidade

Pergunte:

1. O repositório será pessoal, compartilhado ou público?
2. Há algo que deve ficar apenas local ou ser só referenciado, sem copiar?

Explique que 01. SISTEMA/PRIVADO.md é ignorado pelo Git, mas não deve ser usado para segredos que merecem um cofre próprio.

## 6. Revisão obrigatória

Antes de escrever, mostre um resumo com:

~~~markdown
## Proposta de configuração

- Sistema:
- Pessoa/time:
- Propósito:
- Prioridades:
- Trilha:
- Skills prioritárias:
- Fonte de verdade:
- Aprovação humana obrigatória para:
- Limites de privacidade:
- Primeira missão:

Arquivos que vou criar ou atualizar:
- ...
~~~

Pergunte: “Essa configuração representa você? Posso gravar esses arquivos agora?”

Se a resposta não for inequívoca, corrija o resumo ou pare sem escrever.

## 7. Provisionar após aprovação

Atualize somente o necessário:

- 01. SISTEMA/CONTEXTO.md;
- 01. SISTEMA/PERFIL.yaml;
- 01. SISTEMA/SKILLSET.md;
- 01. SISTEMA/ONBOARDING.md;
- 02. MEMORIA/voz-e-estilo.md, se a pessoa forneceu material suficiente.

Use templates/onboarding/PERFIL.template.yaml como estrutura, mas não deixe marcadores {{...}} na versão gerada. Mantenha campos não informados como “a definir”, não invente dados.

No PERFIL.yaml:

- mantenha Codex como rota principal;
- preserve a lista de ações que exigem aprovação;
- marque onboarding.status como active;
- registre as skills prioritárias em skillset.active.

Em SKILLSET.md, escreva o motivo de cada skill prioritária e um próximo uso real.

Em ONBOARDING.md, registre a data, módulos concluídos, lacunas que podem ser retomadas e a primeira missão.

## 8. Fechamento

Entregue:

1. confirmação do nome e da trilha;
2. a primeira missão em três passos pequenos;
3. uma sugestão de skill para iniciar;
4. uma frase de continuidade, por exemplo: “quando quiser se situar de novo, use $overview”.

Ensine pelo uso: contexto antes de ação, decisão antes de acabamento, skill quando houver repetição e automação apenas depois de um fluxo seguro.
