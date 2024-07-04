import os

from bs4 import BeautifulSoup

# 文件夹路径
folder_path = 'D:\HTML\APPHtml'

# 遍历文件夹中的文件
for file_name in os.listdir(folder_path):
    if file_name.endswith('.html'):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r', encoding='UTF-8') as file:
            h5_content = file.read()

        # 使用BeautifulSoup解析H5页面
        soup = BeautifulSoup(h5_content, 'html.parser')

        # 提取页面中的纯文本内容
        text = soup.get_text()

        # 将文本保存到文件中
        text_file_path = os.path.splitext(file_path)[0] + '.txt'
        with open(text_file_path, 'w', encoding='UTF-8') as text_file:
            text_file.write(text)
            print(text_file_path)
