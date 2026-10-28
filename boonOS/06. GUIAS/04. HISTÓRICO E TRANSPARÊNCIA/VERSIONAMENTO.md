# Versões do boonOS

O nome para quem chega é **boonOS Beta**. A partir desta base, cada pacote publicado recebe um identificador técnico para permitir diagnóstico, atualização e comparação de arquivos.

A primeira build desta nova sequência foi `0.1.0-beta.1`; a atual é `0.1.0-beta.8`. Os números da linha anterior, como `2.1.0-beta.4`, foram usados durante a preparação e permanecem no histórico. Eles não indicam que a beta atual seja menos recente. Não escolha a edição apenas comparando esses números antigos com a nova sequência.

## Como evoluir

- Enquanto a mesma versão estiver em pré-lançamento, avance o número após `beta`: por exemplo, `0.1.0-beta.8` para a próxima build.
- Para mudanças futuras, defina o número da versão antes de gerar o pacote: correções incrementam o último número, funcionalidades compatíveis incrementam o número do meio e mudanças incompatíveis incrementam o primeiro. Antes da versão estável `1.0.0`, alterações podem ocorrer durante a beta e precisam ser explicadas nas notas.
- Registre em [CHANGELOG.md](../../CHANGELOG.md) o que mudou, condições de migração e limitações. Atualize `boonos.json`, `01. SISTEMA/CATALOGO.json` e `distribution.json` de forma coerente.
- Publique uma tag e um ZIP para o conteúdo exato testado; não substitua o conteúdo de uma tag ou pacote já publicado. Anote os testes e o que não foi testado.
- O `schema_version` dentro de arquivos de dados indica o formato desses arquivos, não o número comercial da distribuição. Não o mude apenas para renumerar uma release.

Uma instalação personalizada exige backup e avaliação de migração. Leia [Atualizar sem perder seu contexto](<../01. INSTALAÇÃO/ATUALIZAR.md>). O procedimento de publicação está em [Publicar uma edição](<../01. INSTALAÇÃO/PUBLICAR.md>).
