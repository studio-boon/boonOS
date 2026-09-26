---
name: study-playbook
description: >
  Transforma uma referência, aula, vídeo, artigo, livro, case ou exercício em
  aprendizado aplicável: síntese, princípios, prática e playbook pessoal. Use
  quando a pessoa disser "$study-playbook", "quero estudar isso", "resume e me
  ensina", "transforma em exercício", "o que tiro dessa referência?" ou trouxer
  uma fonte para aprender criação, operação ou processo.
---

# study-playbook — estudar para conseguir fazer

## Princípio

Uma referência não vira aprendizado porque foi resumida. Ela vira aprendizado quando gera um critério que a pessoa consegue testar em um trabalho real.

## Entrada

Colete:

- a fonte ou uma descrição confiável dela;
- por que a pessoa quer estudá-la;
- nível atual de familiaridade;
- onde ela gostaria de aplicar o que aprender.

Não invente o conteúdo de uma fonte que não foi fornecida ou que você não conseguiu ler. Diferencie passagem observada, interpretação e hipótese de prática.

## Fluxo

1. **Localize a tese.** Qual ideia, decisão ou técnica torna a fonte interessante?
2. **Separe evidência de opinião.** O que está explícito e o que é sua leitura?
3. **Extraia princípios.** Escreva de três a cinco regras em linguagem simples, sem copiar estilo ou fórmula.
4. **Compare.** Relacione com uma referência que a pessoa já conhece, quando isso ajudar.
5. **Desenhe a prática.** Proponha um exercício pequeno, com limite de tempo e critério de avaliação.
6. **Registre.** Use 05. BIBLIOTECA/01. CRIATIVO/PLAYBOOK-DE-ESTUDO.md se a pessoa quiser guardar a síntese.

## Saída

~~~markdown
## O que esta referência está ensinando

...

## Princípios que vale testar

1. ...

## Exercício de prática

- Faça:
- Limite:
- Critério de sucesso:

## O que observar depois

...
~~~

Se a prática gerar um aprendizado útil, registre origem e escopo com `boon-memoria`. Se indicar mudança no sistema, passe por `boon-melhorar-sistema` antes de criar um novo comando. Se gerar uma peça, siga para `design`; se gerar uma mudança operacional, use a capacidade correspondente no catálogo.
