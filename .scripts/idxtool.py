#!/usr/bin/env python3
import os
import re
import argparse

REPO_ROOT = "/data/data/com.termux/files/home/LLM_Prompts"

def extract_gpt_id(url_or_id):
    match = re.search(r'(g-[A-Za-z0-9]{9}|[A-Za-z0-9]{9})', url_or_id)
    return match.group(1) if match else url_or_id

def generate_toc(root_dir=REPO_ROOT):
    toc_entries = ["# Repository Table of Contents\n\n"]
    for root, dirs, files in sorted(os.walk(root_dir)):
        if "/." in root or root.endswith("/.git") or "/.scripts" in root or "/scripts" in root:
            continue
        rel_path = os.path.relpath(root, root_dir)
        if rel_path == ".":
            continue
        depth = rel_path.count(os.sep)
        indent = "  " * depth
        folder = os.path.basename(root)
        toc_entries.append(f"{indent}- **{folder}/**\n")
        
        sub_toc = [f"# {folder} Index\n\n"]
        for file in sorted(files):
            if file.endswith((".md", ".txt")) and file not in ["README.md", "TOC.md"]:
                file_rel = os.path.join(rel_path, file)
                toc_entries.append(f"{indent}  - [{file}]({file_rel})\n")
                sub_toc.append(f"- [{file}]({file})\n")
        
        if len(sub_toc) > 1:
            with open(os.path.join(root, "TOC.md"), "w", encoding="utf-8") as f:
                f.writelines(sub_toc)

    with open(os.path.join(root_dir, "TOC.md"), "w", encoding="utf-8") as f:
        f.writelines(toc_entries)
    print("Successfully generated TOC.md at root and subdirectories.")

def find_gpt(query, root_dir=REPO_ROOT):
    target_id = extract_gpt_id(query)
    found = False
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if target_id.lower() in file.lower():
                print(f"Found in filename: {os.path.join(root, file)}")
                found = True
                continue
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    if target_id in content:
                        print(f"Found inside content: {file_path}")
                        found = True
            except Exception:
                pass
    if not found:
        print(f"No results found for query: {query}")

def generate_template(url, output_dir=os.path.join(REPO_ROOT, "Custom Instructions")):
    gpt_id = extract_gpt_id(url)
    filename = f"{gpt_id}_New_Prompt.md"
    target_path = os.path.join(output_dir, filename)
    template_content = f"""---
id: "{gpt_id}"
url: "{url}"
title: "New Prompt Title"
category: "Custom Instructions"
version: "1.0"
---

# System Prompt

[Insert System Prompt Here]

## Instructions & Constraints
- Constraint 1
- Constraint 2
"""
    os.makedirs(output_dir, exist_ok=True)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(template_content)
    print(f"Scaffolded new prompt template at: {target_path}")

def normalize_filename(file_path):
    directory, basename = os.path.split(file_path)
    name, ext = os.path.splitext(basename)
    sanitized = re.sub(r'[^A-Za-z0-9_\-]', '_', name)
    new_path = os.path.join(directory, f"{sanitized}{ext}")
    if file_path != new_path:
        os.rename(file_path, new_path)
        print(f"Renamed {file_path} -> {new_path}")

def main():
    parser = argparse.ArgumentParser(description="LLM_Prompts Repository Management Tool")
    parser.add_argument("--toc", action="store_true", help="Generate hierarchical TOC.md files")
    parser.add_argument("--find-gpt", type=str, help="Find prompt file by GPT ID or URL")
    parser.add_argument("--template", type=str, help="Scaffold a new prompt file from URL")
    parser.add_argument("--rename", type=str, help="Normalize/sanitize a target filename")
    
    args = parser.parse_args()
    if args.toc:
        generate_toc()
    elif args.find_gpt:
        find_gpt(args.find_gpt)
    elif args.template:
        generate_template(args.template)
    elif args.rename:
        normalize_filename(args.rename)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
