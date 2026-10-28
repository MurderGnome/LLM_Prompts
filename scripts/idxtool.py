#!/usr/bin/env python3
import os

def generate_index():
    repo_dir = "/data/data/com.termux/files/home/LLM_Prompts"
    toc_path = os.path.join(repo_dir, "TOC.md")
    lines = ["# LLM Prompts Repository Index\n\n"]

    for root, dirs, files in sorted(os.walk(repo_dir)):
        # Skip hidden directories like .git
        if "/." in root or root.endswith("/.git"):
            continue

        rel_path = os.path.relpath(root, repo_dir)
        if rel_path == "." or rel_path == "scripts":
            continue

        depth = rel_path.count(os.sep)
        indent = "  " * depth
        folder_name = os.path.basename(root)
        lines.append(f"{indent}- **{folder_name}/**\n")

        for file_name in sorted(files):
            if file_name.endswith((".txt", ".md", ".docx", ".PDF")) and file_name not in ["README.md", "TOC.md"]:
                file_rel = os.path.join(rel_path, file_name)
                lines.append(f"{indent}  - [{file_name}]({file_rel})\n")

    with open(toc_path, "w") as f:
        f.writelines(lines)
    print(f"Index successfully updated at {toc_path}")

if __name__ == "__main__":
    generate_index()
