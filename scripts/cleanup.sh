#!/data/data/com.termux/files/usr/bin/bash
set -e

REPO_DIR="/data/data/com.termux/files/home/LLM_Prompts"
cd "$REPO_DIR"

echo "Starting repository cleanup..."

if [ -f "GPT Magic Words.txt" ]; then
    mkdir -p "Meta Prompts"
    mv "GPT Magic Words.txt" "Meta Prompts/"
    echo "Moved GPT Magic Words.txt to Meta Prompts/"
fi

if [ -f "KB Query and Adherence.txt" ]; then
    mkdir -p "Custom Instructions"
    mv "KB Query and Adherence.txt" "Custom Instructions/"
    echo "Moved KB Query and Adherence.txt to Custom Instructions/"
fi

if [ -d "Markdown Course Material" ]; then
    mkdir -p "Course Development/Markdown Course Material"
    mv "Markdown Course Material/"* "Course Development/Markdown Course Material/" 2>/dev/null || true
    rmdir "Markdown Course Material" 2>/dev/null || true
    echo "Consolidated Markdown Course Material directory"
fi

if [ -f "GPT-Prompts-main.zip" ]; then
    rm -f "GPT-Prompts-main.zip"
    echo "Removed GPT-Prompts-main.zip"
fi

echo "Cleanup completed successfully."
