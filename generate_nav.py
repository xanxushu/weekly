import os
import re
import yaml

# 定义 docs 文件夹路径
docs_path = 'docs'

# 获取所有文件和目录
entries = os.listdir(docs_path)

# 定义正则表达式来匹配期刊文件名
issue_pattern = re.compile(r'^issue-(\d+)\.md$')

# 用于存储文章和其他文件
articles = []
others = []

# 遍历 docs 目录中的文件和目录
for entry in sorted(entries):
    entry_path = os.path.join(docs_path, entry)
    if os.path.isfile(entry_path):
        match = issue_pattern.match(entry)
        if match:
            # 将文件名转换为“第N期”
            issue_number = int(match.group(1))
            articles.append({'第{}期'.format(issue_number): entry})
        else:
            # 非期刊文件进行翻译
            title = entry.split('.')[0]
            translated_title = {
                'new': '新',  # 在此处添加更多翻译
            }.get(title, title)  # 默认使用原名称
            others.append({translated_title: entry})

# 创建 nav 配置
nav_entries = [{'文章': articles}, {'其他': others}]

# 更新 mkdocs.yml 配置文件
with open('mkdocs.yml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# 更新导航配置
config['nav'] = [{'首页': 'index.md'}] + nav_entries

# 写入更新后的配置
with open('mkdocs.yml', 'w', encoding='utf-8') as f:
    yaml.safe_dump(config, f, allow_unicode=True)
