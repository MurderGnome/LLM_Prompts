#!/data/data/com.termux/files/usr/bin/bash
set -e

SOURCE_REPO="/data/data/com.termux/files/home/chatgpt_system_prompt"
TARGET_REPO="/data/data/com.termux/files/home/LLM_Prompts"

echo "Pulling official product system prompts..."
mkdir -p "$TARGET_REPO/Custom Instructions/Official_Products"
cp -r "$SOURCE_REPO/prompts/official-product/"* "$TARGET_REPO/Custom Instructions/Official_Products/"

echo "Pulling open-source project system prompts..."
mkdir -p "$TARGET_REPO/Computers/OpenSource_Agents"
cp -r "$SOURCE_REPO/prompts/opensource-prj/"* "$TARGET_REPO/Computers/OpenSource_Agents/"

echo "Pulling security guardrails..."
mkdir -p "$TARGET_REPO/Meta Prompts"
cp "$SOURCE_REPO/SECURITY.md" "$TARGET_REPO/Meta Prompts/Security_Guardrails.md"

echo "Processing metadata and synchronizing repository..."
bash /data/data/com.termux/files/home/LLM_Prompts/scripts/sync_repo.sh

echo "Import and synchronization complete."
