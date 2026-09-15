# Personalizar sem quebrar o template

## Dar um nome ao sistema

O nome fica em 01. SISTEMA/CONTEXTO.md e em 01. SISTEMA/PERFIL.yaml. O $init faz isso por você, mas os dois arquivos podem ser editados depois.

## Ensinar voz e gosto

Adicione exemplos reais e comentários em 02. MEMORIA/voz-e-estilo.md. Diga também o que você não quer: clichês, referências copiadas, tom excessivamente formal, excesso de efeito ou frases vagas.

## Ajustar a trilha

Em 01. SISTEMA/SKILLSET.md, mantenha poucas skills ativas e escreva por que cada uma importa agora. As outras continuam disponíveis. Uma vez por mês, revise o que está realmente sendo usado.

## Criar uma skill sua

Chame $skill-creator quando:

- uma tarefa se repetiu;
- há uma saída que você quer manter consistente;
- um checklist evita erros;
- há uma decisão que depende sempre dos mesmos critérios.

Não crie skill para uma tarefa única. Antes, experimente o fluxo com as skills existentes.

## Manter o que é privado fora do Git

Use 01. SISTEMA/PRIVADO.md para notas locais e 03. DOCS/_PRIVADO/ para documentos locais confidenciais. Ambos já estão no .gitignore. Para fontes sensíveis, prefira links ou uma referência de localização em vez de copiar o conteúdo para o repositório. Arquivo ignorado não é cofre: segredos devem ficar em um gerenciador apropriado.
