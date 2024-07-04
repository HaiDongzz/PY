#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/1 15:23
# @Author  : HD
# @File    : Email.py
# @Description :


# 单位M，单个附件大小
import logging
import os
import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from Conf.config import smtp_cfg, email_cfg

_FILESIZE = 20
# 附件数量
_FILECOUNT = 10
_smtp_cfg = smtp_cfg
_email_cfg = email_cfg
_logger = logging.getLogger('main.email')


class Email:
    def __init__(self, subject, context=None, attachment=None):
        self._smtp_cfg = email_cfg
        self._email_cfg = email_cfg
        self.subject = subject
        self.context = context
        self.attachment = attachment
        self.message = MIMEMultipart()
        self._message_init()

    def _message_init(self):
        if self.subject:
            # 邮件标题
            self.message['subject'] = Header(self.subject, 'utf-8')
        else:
            raise ValueError("无效主题")
        # 发件人
        self.message['from'] = _email_cfg['sender']
        # 收件人
        self.message['to'] = _email_cfg['receivers']

        if self.context:
            # 邮件正文
            self.message.attach(MIMEText(self.context, 'html', 'utf-8'))
        # 邮件附件
        if self.attachment:
            if isinstance(self.attachment, str):
                self._attach(self.attachment)
            if isinstance(self.attachment, list):
                count = 0
                for each in self.attachment:
                    if count <= _FILECOUNT:
                        self._attach(each)
                        count += 1
                    else:
                        _logger.warning(f'附件超过：,{_FILECOUNT}')
                        break

    def _attach(self, file):
        if os.path.isfile(file) and os.path.getsize(file) <= _FILESIZE * 1024 * 1024:
            attach = MIMEApplication(open(file, 'rb').read())
            attach.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            attach["Content-Type"] = 'application/octet-stream'
            self.message.attach(attach)
        else:
            _logger.error(f'附件不存在或超过{_FILESIZE}M:{file}')

    def send_mail(self):
        s = smtplib.SMTP_SSL(_smtp_cfg['host'], int(_smtp_cfg['port']))
        result = True
        try:
            s.login(_smtp_cfg['user'], _smtp_cfg['passwd'])
            s.sendmail(_email_cfg['sender'], _email_cfg['receivers'], self.message.as_string())
        except smtplib.SMTPException as e:
            result = False
            _logger.error('邮件发送失败', exc_info=True)
        finally:
            s.close()
        return result


# 初始化调用

mail = Email('Subject', 'Body text', ['E:\\桌面\\data.xlsx'])
send = mail.send_mail()
print(send)
