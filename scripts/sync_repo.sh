#!/data/data/com.termux/files/usr/bin/bash
set -e

REPO_DIR="/data/data/com.termux/files/home/LLM_Prompts"
cd "$REPO_DIR"

echo "Running repository maintenance..."
bash /data/data/com.termux/files/home/LLM_Prompts/scripts/cleanup.sh
python3 /data/data/com.termux/files/home/LLM_Prompts/scripts/idxtool.py

echo "Syncing changes with GitHub..."
git add .
git commit -m "Automated repository overhaul and index update" || echo "No changes to commit"
git push origin main

echo "Repository synchronized successfully."
