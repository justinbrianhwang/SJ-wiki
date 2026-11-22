#!/bin/bash
# Runs codex expand3 groups, 5 in parallel; skips groups already done.
cd "f:/coding/Web/SJ Wiki"
touch tools/codex-logs/expand3-done.txt
ls tools/codex-prompts/expand3/*.md | xargs -P 5 -I{} bash -c '
  g=$(basename {} .md)
  grep -q "^$g exit=0" tools/codex-logs/expand3-done.txt && exit 0
  codex exec -s workspace-write --skip-git-repo-check - < {} > tools/codex-logs/expand3-$g.log 2>&1
  echo "$g exit=$?" >> tools/codex-logs/expand3-done.txt'
echo ALL_DONE
