#!/bin/bash
# Runs codex expansion groups, 4 in parallel.
cd "f:/coding/Web/SJ Wiki"
mkdir -p tools/codex-logs
ls tools/codex-prompts/expand2/*.md | xargs -P 4 -I{} bash -c '
  g=$(basename {} .md)
  codex exec -s workspace-write --skip-git-repo-check - < {} > tools/codex-logs/expand2-$g.log 2>&1
  echo "$g exit=$?" >> tools/codex-logs/expand2-done.txt'
echo ALL_DONE
