#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
agents_dir="$repo_root/.agents/skills"
claude_dir="$repo_root/.claude/skills"
expected_skills="brand-storytelling carrossel content-strategy copywriting design design-review grill-me image-direction init interface-polish overview portfolio-case-study post-social presentation router site-design skill-creator study-playbook taste writing-filter"
expected_total=20
actual_total=0
status=0

for required_file in AGENTS.md "00. COMECE-AQUI.md" "01. SISTEMA/CONTEXTO.md" "01. SISTEMA/PERFIL.yaml" "01. SISTEMA/ONBOARDING.md" "01. SISTEMA/SKILLSET.md" docs/INSTALAR.md docs/MINDSET.md docs/SKILLS.md; do
  if [[ ! -f "$repo_root/$required_file" ]]; then
    echo "Arquivo essencial ausente: $required_file" >&2
    status=1
  fi
done

for expected_skill in $expected_skills; do
  if [[ ! -f "$agents_dir/$expected_skill/SKILL.md" ]]; then
    echo "Skill esperada ausente: $expected_skill" >&2
    status=1
  fi
done

for skill_dir in "$agents_dir"/*; do
  if [[ ! -d "$skill_dir" || ! -f "$skill_dir/SKILL.md" ]]; then
    continue
  fi

  actual_total=$((actual_total + 1))
  skill_file="$skill_dir/SKILL.md"
  folder_name="$(basename "$skill_dir")"
  declared_name="$(awk 'NR == 1 { next } /^---$/ { exit } /^name:/ { sub(/^name:[[:space:]]*/, ""); print; exit }' "$skill_file")"

  if [[ "$(head -n 1 "$skill_file")" != "---" ]]; then
    echo "Frontmatter ausente: $skill_file" >&2
    status=1
  fi

  if ! rg -q '^name: [a-z0-9-]+$' "$skill_file"; then
    echo "Campo name ausente ou inválido: $skill_file" >&2
    status=1
  fi

  if [[ "$declared_name" != "$folder_name" ]]; then
    echo "Name e pasta divergem: $folder_name / $declared_name" >&2
    status=1
  fi

  if ! rg -q '^description:' "$skill_file"; then
    echo "Campo description ausente: $skill_file" >&2
    status=1
  fi

  if ! rg -q --fixed-strings "\$$folder_name" "$repo_root/docs/SKILLS.md"; then
    echo "Skill não está documentada em docs/SKILLS.md: $folder_name" >&2
    status=1
  fi
done

if [[ "$actual_total" -ne "$expected_total" ]]; then
  echo "Quantidade inválida de skills: esperadas $expected_total, encontradas $actual_total" >&2
  status=1
fi

if [[ ! -d "$claude_dir" ]]; then
  echo "Espelho Claude ausente: $claude_dir" >&2
  exit 1
fi

if ! diff -qr "$agents_dir" "$claude_dir"; then
  echo "Os espelhos .agents e .claude diferem." >&2
  status=1
fi

if ! rg -q --fixed-strings '$init' "$repo_root/00. COMECE-AQUI.md"; then
  echo "O guia inicial não referencia o onboarding $init." >&2
  status=1
fi

if [[ "$status" -eq 0 ]]; then
  echo "Estrutura Codex-first válida: 20 skills documentadas e espelhos em paridade."
fi

exit "$status"
