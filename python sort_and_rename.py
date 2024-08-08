import os
import re

docs_dir = "docs"
mkdocs_yml = "mkdocs.yml"

# 获取 docs 目录中的文件列表并进行排序
files = sorted(
    [f for f in os.listdir(docs_dir) if f.startswith("issue-") and f.endswith(".md")],
    key=lambda x: int(re.search(r'\d+', x).group()),
    reverse=True  # 倒序排列
)

# 生成文件索引和新文件名
nav_entries = []
for filename in files:
    issue_num = re.search(r'\d+', filename).group()
    new_filename = f"第{issue_num}期.md"
    os.rename(os.path.join(docs_dir, filename), os.path.join(docs_dir, new_filename))
    nav_entries.append(f"  - '第{issue_num}期': {new_filename}")

# 更新 mkdocs.yml
with open(mkdocs_yml, "r") as file:
    lines = file.readlines()

nav_start = lines.index("nav:\n") + 1
nav_end = len(lines)

new_lines = lines[:nav_start] + nav_entries + lines[nav_end:]

with open(mkdocs_yml, "w") as file:
    file.writelines(new_lines)
