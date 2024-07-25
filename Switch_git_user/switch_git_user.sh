#!/bin/bash
if [ "$1" = "school" ]; then
  git config user.name "Cchancee"
  git config user.email "c.karambizi@alustudent.com"
elif [ "$1" = "personal" ]; then
  git config user.name "24chance"
  git config user.email "chanceown@gmaile.com"
else
  echo "Usage: ./switch_git_user.sh [school|personal]"
fi
