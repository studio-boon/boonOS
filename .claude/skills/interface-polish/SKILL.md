---
name: interface-polish
description: >
  Melhora detalhes de interfaces digitais: componentes, tipografia, espaçamento,
  bordas, sombras, estados, microinterações, animações, responsividade e sensação
  de produto. Use quando o usuário disser "polir UI", "make it feel better",
  "a interface está estranha", "ajusta os detalhes", hover, active state,
  motion, radius, shadow, optical alignment ou microinteração.
---

# interface-polish

Use esta skill para detalhes que fazem uma interface parecer mais bem acabada.

## Princípios

- Alinhamento óptico vence alinhamento matemático quando o olho percebe errado.
- Raio externo deve conversar com raio interno e padding.
- Sombra precisa parecer ambiente, não contorno escuro.
- Animação de interação deve ser interrompível e curta.
- Estado de hover, foco, active, loading, empty e error fazem parte do componente.
- Texto e números não podem causar layout shift.
- Reduzir movimento quando `prefers-reduced-motion` estiver ativo.

## Revisão

Checar:

- tipografia: line-height, tracking, largura de linha, truncamento;
- espaçamento: grupos claros, padding consistente, densidade adequada;
- superfície: borda, sombra, raio e contraste;
- movimento: duração, easing, origem da transformação;
- estados: hover, focus, active, disabled, loading, empty, error;
- responsividade: toque, quebra de texto, overflow e altura dinâmica;
- acessibilidade: foco visível, contraste, labels e semântica.

## Formato obrigatório para revisão

Usar tabela:

| Antes | Depois | Por quê |
|---|---|---|
| `transition: all 300ms` | `transition: transform 180ms ease-out, opacity 180ms ease-out` | Evita animar propriedades erradas |

Depois da tabela, listar no máximo 5 mudanças prioritárias.

## Regra

Não transformar polimento em redesign. Se a estrutura, navegação ou promessa visual estiverem quebradas, encaminhar para `/site-design` ou `/design-review`.
