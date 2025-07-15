import pyperclip
import time
import os
from datetime import datetime

def get_last_saved_text(log_file):
    if not os.path.exists(log_file):
        return ""
    with open(log_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        # 查找最后一条剪切内容
        for line in reversed(lines):
            if line.strip():
                return line.rstrip("\n")
    return ""

def main():
    log_file = "clipboard_log.txt"
    content_log_file = "content_log.txt"
    last_text = get_last_saved_text(log_file)
    print("正在监听剪贴板内容，每次复制都会自动保存到 clipboard_log.txt 和 content_log.txt ...")
    while True:
        try:
            text = pyperclip.paste()
            if text and text != last_text:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # clipboard_log.txt 记录时间和内容
                with open(log_file, "a", encoding="utf-8") as log:
                    log.write(f"剪切时间: {now}\n剪切内容: {text}\n\n")
                # content_log.txt 只记录内容
                with open(content_log_file, "a", encoding="utf-8") as content_log:
                    content_log.write(f"{text}\n")
                print(f"已保存: {text}  剪切时间: {now}")
                last_text = text
            time.sleep(1)  # 降低CPU占用
        except KeyboardInterrupt:
            print("已退出。")
            break

if __name__ == "__main__":
    main()
