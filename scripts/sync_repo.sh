#!/data/data/com.termux/files/usr/bin/bash
set -e

REPO_DIR="/data/data/com.termux/files/home/LLM_Prompts"
cd "$REPO_DIR"

echo "Executing cleanup..."
bash /data/data/com.termux/files/home/LLM_Prompts/scripts/cleanup.sh

echo "Injecting metadata headers..."
python3 /data/data/com.termux/files/home/LLM_Prompts/scripts/add_yaml.py

echo "Updating index..."
python3 /data/data/com.termux/files/home/LLM_Prompts/.scripts/idxtool.py --toc

echo "Syncing with GitHub..."
git add .
git commit -m "Automated update of repository structure and TOC" || echo "No changes to commit"
git push origin main

echo "Sync complete."
