#!/bin/bash
# Runs codex final groups, 5 in parallel; skips groups already done.
cd "f:/coding/Web/SJ Wiki"
touch tools/codex-logs/final-done.txt
ls tools/codex-prompts/final/*.md | xargs -P 5 -I{} bash -c '
  g=$(basename {} .md)
  grep -q "^$g exit=0" tools/codex-logs/final-done.txt && exit 0
  codex exec -s workspace-write --skip-git-repo-check - < {} > tools/codex-logs/final-$g.log 2>&1
  echo "$g exit=$?" >> tools/codex-logs/final-done.txt'
echo ALL_DONE
