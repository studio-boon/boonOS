---
name: writing-filter
description: >
  Filtro base de escrita para revisar ou criar textos sem impor uma voz fixa.
  Use quando o usuário pedir copy, post, site, proposta, roteiro, manifesto,
  texto de portfolio, mensagem comercial, revisão de tom, "melhora esse texto",
  "deixa mais claro", "deixa com minha voz" ou "passa um filtro".
---

# writing-filter

Filtro neutro de escrita. A função é deixar o texto mais claro, específico e útil sem transformar tudo em uma voz genérica.

## Regra central

A voz vem do usuário, não da skill.

Antes de escrever ou revisar, procurar:

- preferências em `CLAUDE.md`;
- `_02. MEMORIA/voz-e-estilo.md`, se existir;
- exemplos de texto enviados na conversa;
- contexto do público, canal e objetivo.

Se não houver voz definida, usar tom claro, direto e específico.

## Briefing mínimo

Se não estiver claro, perguntar:

- Quem vai ler?
- Qual ação ou percepção o texto precisa gerar?
- Onde o texto será usado?
- Existe algum exemplo de tom a seguir ou evitar?

## Passagem de revisão

Revisar por:

- clareza: a ideia principal aparece rápido;
- especificidade: evitar frases que servem para qualquer pessoa ou marca;
- consequência: trocar ênfase abstrata por efeito concreto;
- ritmo: cortar repetição, enchimento e sequência automática de três ideias;
- voz: preservar palavras, cadência e ponto de vista do usuário;
- canal: adequar densidade para post, site, proposta, e-mail, roteiro ou deck.

## Cortes padrão

Remover ou reescrever:

- adjetivo sem prova;
- promessa vaga;
- frase de autoridade vazia;
- empatia performática;
- abertura longa antes do ponto;
- CTA genérico;
- metáfora decorativa que não ajuda a entender.

## Formato de saída

Quando revisar, entregar:

```text
Versão revisada:
[texto]

O que mudou:
- [mudança importante]
- [mudança importante]
```

Quando criar do zero, entregar a versão final e, se fizer sentido, 2 ou 3 alternativas de tom.
