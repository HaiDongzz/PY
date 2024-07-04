#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/10 15:44
# @Author  : HD
# @File    : QQ_mail.py
# @Description :


import smtplib
from email.header import Header
from email.mime.text import MIMEText

# SMTP服务器地址和端口，这里以QQ邮箱为例
smtp_server = 'smtp.qq.com'
smtp_port = 587

# 发件人邮箱账号和密码
sender_email = 'haidongzz@qq.com'
sender_password = 'ywdgtqjekkdmjhbi'

# 收件人邮箱账号
receiver_email = '1451666963@qq.com'

# 构建邮件主题、内容和头部信息
email_subject = '推送邮件'
email_body = '你好，这是一封推送邮件。'
email_content = MIMEText(email_body, 'plain', 'utf-8')
email_content['Subject'] = Header(email_subject, 'utf-8')
email_content['From'] = sender_email
email_content['To'] = receiver_email

# 连接SMTP服务器并进行身份验证
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # 开启TLS加密
    server.login(sender_email, sender_password)  # 登录SMTP服务器
    server.sendmail(sender_email, [receiver_email], email_content.as_string())  # 发送邮件

print('邮件发送成功')

# ywdgtqjekkdmjhbi
