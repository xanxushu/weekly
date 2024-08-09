import os
import re
import yaml

docs_dir = "docs"
mkdocs_yml = "mkdocs.yml"

# 获取 docs 目录中的文件列表
files = [
    f for f in os.listdir(docs_dir)
    if f.startswith("issue-") and f.endswith(".md")
]

# 提取期刊号并进行排序
files_with_numbers = [
    (f, int(re.search(r'\d+', f).group())) for f in files
]

# 按照期刊号排序
files_with_numbers.sort(key=lambda x: x[1], reverse=True)

# 生成文件索引和新文件名（使用零填充）
nav_entries = []
for original_filename, issue_num in files_with_numbers:
    new_filename = f"issue-{issue_num:03}.md"
    os.rename(
        os.path.join(docs_dir, original_filename),
        os.path.join(docs_dir, new_filename)
    )
    nav_entries.append({'第{}期'.format(issue_num): new_filename})

# 更新 mkdocs.yml
with open(mkdocs_yml, "r") as file:
    config = yaml.safe_load(file)

# 更新导航栏条目
config['nav'] = [{'Home': 'index.md'}] + nav_entries

with open(mkdocs_yml, "w") as file:
    yaml.dump(config, file, allow_unicode=True, default_flow_style=False)