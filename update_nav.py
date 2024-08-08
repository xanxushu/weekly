import os
import shutil

def copy_readme_to_index():
    readme_path = "README.md"
    index_path = "docs/index.md"
    if os.path.exists(readme_path):
        shutil.copy(readme_path, index_path)
        print(f"Copied {readme_path} to {index_path}")
    else:
        print(f"{readme_path} not found!")

def generate_nav():
    docs_path = "docs"
    files = sorted(os.listdir(docs_path))
    nav_entries = ["  - 首页: index.md", "  - 文章:"]

    for file in files:
        if file.endswith(".md") and file != "index.md":
            issue_name = os.path.splitext(file)[0]
            nav_entries.append(f"    - {issue_name}: {file}")

    return "\n".join(nav_entries)

def update_mkdocs_yml():
    mkdocs_path = "mkdocs.yml"
    with open(mkdocs_path, "r") as f:
        lines = f.readlines()

    with open(mkdocs_path, "w") as f:
        nav_updated = False
        for line in lines:
            if line.strip().startswith("nav:"):
                f.write("nav:\n")
                f.write(generate_nav())
                f.write("\n")
                nav_updated = True
            else:
                f.write(line)
        
        if not nav_updated:
            f.write("nav:\n")
            f.write(generate_nav())
            f.write("\n")

if __name__ == "__main__":
    copy_readme_to_index()
    update_mkdocs_yml()
