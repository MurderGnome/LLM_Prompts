#!/usr/bin/env python3
import os

REPO_DIR = "/data/data/com.termux/files/home/LLM_Prompts"

def add_yaml_header(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    if content.startswith("---"):
        print(f"Skipping (already has YAML): {file_path}")
        return

    rel_path = os.path.relpath(file_path, REPO_DIR)
    parts = rel_path.split(os.sep)
    category = parts[0] if len(parts) > 1 else "General"
    file_name = os.path.basename(file_path)
    title = os.path.splitext(file_name)[0].replace("_", " ").replace("-", " ").title()

    yaml_header = f"""---
title: "{title}"
category: "{category}"
target_models: ["GPT-4o", "Claude 3.5 Sonnet"]
version: "1.0"
---

"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(yaml_header + content)
    print(f"Added YAML header to: {file_path}")

def main():
    for root, dirs, files in os.walk(REPO_DIR):
        if "/." in root or root.endswith("/.git") or "/scripts" in root or "/.scripts" in root:
            continue
        for file in files:
            if file.endswith((".txt", ".md")) and file not in ["README.md", "TOC.md"]:
                full_path = os.path.join(root, file)
                add_yaml_header(full_path)

if __name__ == "__main__":
    main()
