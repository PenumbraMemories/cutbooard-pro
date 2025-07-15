import re

with open("clipboard_log.txt", "r", encoding="utf-8") as f:
    content = f.read()

links = re.findall(r"https://pan\.baidu\.com/s/[^\s]+", content)

with open("baidu_links.txt", "w", encoding="utf-8") as f:
    for link in links:
        f.write(link + "\n")

print("已提取所有百度网盘链接到 baidu_links.txt")