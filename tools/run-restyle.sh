#!/bin/bash
# Runs codex restyle groups, 5 in parallel; skips groups already done.
cd "f:/coding/Web/SJ Wiki"
touch tools/codex-logs/restyle-done.txt
ls tools/codex-prompts/restyle/*.md | xargs -P 5 -I{} bash -c '
  g=$(basename {} .md)
  grep -q "^$g exit=0" tools/codex-logs/restyle-done.txt && exit 0
  codex exec -s workspace-write --skip-git-repo-check - < {} > tools/codex-logs/restyle-$g.log 2>&1
  echo "$g exit=$?" >> tools/codex-logs/restyle-done.txt'
echo ALL_DONE
