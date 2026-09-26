# Validação do boonOS 2.1 beta

Registro inicial: 25/09/2026. Esta beta tem validação técnica e exemplos fictícios. Não equivale a uso continuado por pessoas novas, contabilidade oficial ou integração externa ativa.

## Como reproduzir

Na raiz, com Python 3.10 ou superior:

```sh
python3 scripts/check.py --release
python3 -m unittest discover -s tests -v
python3 scripts/finance.py "06. GUIAS/03. EXEMPLOS/operacao.json" --as-of 2026-09-25
python3 scripts/package.py boonOS-2.1-beta.zip
```

Em uma instalação personalizada, use `check.py` sem `--release`: a verificação de release compara os arquivos aos hashes da distribuição original, que naturalmente mudam quando o contexto é preenchido.

## Evidências locais

- Scripts executados em macOS com Python 3.14.4, usando apenas a biblioteca padrão.
- Casos financeiros cobrem parcial, estorno, cancelamento, duplicação, datas, valores inválidos, precisão, ausência de dados, conciliação por ID e ambiguidades sem baixa automática.
- O exemplo fictício de 25/09 tem caixa gerencial de 1.700,00; comprometido a receber de 1.400,00; a pagar de 500,00. Previsões de 900,00 e 200,00 são apresentadas separadamente.
- Melhoria: candidato preparado, aplicação, no-op e reversão executados em cópia isolada, com restauração dos bytes originais. Drift e falhas de escrita preservam ou restauram os arquivos conforme os testes.
- Migração exercitada com árvores Git do starter (`91b1002`) e da beta 2.0 (`982db29`), com verificação de origem inalterada e paridade no destino. Casos de colisão e customização também são testados.
- Exportação cobre recusa de arquivo alterado e exclusão de dados não incluídos na allowlist.
- O checker verifica arquivos essenciais, frontmatter, catálogo, links e espelhos; não reprova uma extensão pessoal válida por aumentar a quantidade.
- Avaliação conversacional com agentes em cópias isoladas: entrada sem contexto, três perguntas iniciais, checkpoint autorizado e pausa; uma nova sessão retomou o resumo, produziu plano semanal e uma hipótese criativa. O plano calculou 16h de demanda em 18h disponíveis e manteve o projeto dependente de referências como condicional. Nenhuma mensagem, conta externa ou envio foi executado. É uma simulação no ambiente Codex desta avaliação, não um teste independente no aplicativo Claude Code.
- A revisão adversarial encontrou e corrigiu três casos: exclusão pessoal do Git após renomeação de raiz, colisão de caixa/Unicode com o manifesto de migração e alteração de bytes entre validação e exportação. Os casos viraram testes de regressão.

A contagem vigente de testes está na saída do comando e no GitHub Actions. Os testes verificam invariantes e resultados; não medem por si só a qualidade de toda resposta de um agente.

## Compatibilidade e integração

O workflow `.github/workflows/check.yml` está ativo. A primeira execução completa, no commit `36fb9cc`, passou nas seis combinações de Linux, macOS e Windows com Python 3.10 e 3.13: [resultado da matriz](https://github.com/tchelove/boonOS/actions/runs/36204735331). Cada combinação executou estrutura/hashes, suíte de testes, exemplo financeiro e exportação. Para a revisão que você estiver usando, confira também o commit exato em [GitHub Actions](https://github.com/tchelove/boonOS/actions). Consulte [manter CI](<06. GUIAS/01. INSTALAÇÃO/ATIVAR-CI.md>) ao configurar outra cópia.

Os contratos de entrada para Codex, Claude Code e Gemini CLI estão incluídos. Gemini importa o contrato comum e usa a mesma árvore .agents/skills, conforme a documentação oficial; não foi executado um onboarding no aplicativo Gemini CLI nesta avaliação. Descoberta de skills, autenticação, geração de mídia e experiência do aplicativo dependem da versão e dos recursos instalados. Um teste do núcleo Python no Windows não comprova um onboarding completo no aplicativo Windows.

O roteiro de [onboarding](<06. GUIAS/03. EXEMPLOS/ONBOARDING.md>) permite testar conversa, checkpoint e retomada. O exemplo de [criação](<06. GUIAS/03. EXEMPLOS/CRIACAO.md>) separa direção, artefato e aprovação. Testes simulados com agentes não substituem a observação de alguém instalando pela primeira vez.

## Limites desta edição

- O financeiro é gerencial, de uma moeda e com saldo inicial informado; não autentica extratos nem executa transações. Não contém legislação, cálculo fiscal automático ou escrituração oficial.
- `improve.py` verifica integridade, não ganho de qualidade. A avaliação funcional tem registro separado; escrita é atômica por arquivo, não uma transação multi-arquivo resistente a interrupção abrupta.
- A migração cria outro workspace. Dados pessoais e arquivos legados preservados podem exigir revisão de contexto e links; o código antigo não é executado.
- O exportador aceita apenas uma release íntegra. Não é ferramenta de backup ou publicação de um workspace personalizado.
- Agendamento e integrações começam desligados. Nenhum modelo, servidor, canal ou assinatura é instalado por clonar o template.
