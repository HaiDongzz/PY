from bs4 import BeautifulSoup

# 读取H5文件
with open('D:\\HTML\\APPHtml\\appDetails_contrabandAgreement.html', 'r', encoding='UTF-8') as file:
    h5_content = file.read()

# 使用BeautifulSoup解析H5页面
soup = BeautifulSoup(h5_content, 'html.parser')

# 提取页面中的纯文本内容
text = soup.get_text()

# 输出文本内容
print(text)

with open('D:\\HTML\\workspace\\appDetails_contrabandAgreement.txt', 'w', encoding='UTF-8') as file:
    file.write(text)
