import re

def update_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 匹配 docs/issue-num.md 格式的链接
    def replace_link(match):
        issue_number = match.group(1)
        return f'issue-{int(issue_number):03}.md'

    # 替换链接
    updated_content = re.sub(r'docs/issue-(\d+).md', replace_link, content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

# 更新 README.md 中的链接
update_links('README.md')