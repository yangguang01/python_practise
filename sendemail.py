#! /usr/bin/env python
# coding=utf-8

import smtplib
import os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def main():
    sender = 'yangg062@gmail.com'
    # 开启gmail应用密码即可发送
    input_pwd = raw_input('password: ')
    sender_pwd = input_pwd    # 直接接受密码会有\n后缀无法登陆
    smtp_server = 'smtp.gmail.com'

    all_receivers = []
    print 'Enter receiver: '
    while True:
        input_receivers = raw_input('> ')
        if input_receivers == '':
            break
        else:
            all_receivers.append(input_receivers)
    receivers = all_receivers

    # input_receivers = raw_input('Enter receiver: ')
    # receivers = input_receivers

    message = MIMEMultipart()
    message['Subject'] = '分享资料01'
    message['From'] = sender
    message['To'] = ''
    message['Cc'] = ''
    message['Bcc'] = ','.join(receivers)

    mail_body = '''
    附件是“给产品经理讲技术“的文章汇总电子书

    当然，这封邮件的最重要的目的是实现了通过python发邮件。使用了SMTP功能，神奇的是这么发邮件不用翻墙。

    '''
    # 将正文放到邮件结构里
    message.attach(MIMEText(mail_body, 'plain', 'utf-8'))

    # 附件路径
    input_filepath = raw_input('Enter filepath: ')
    if input_filepath != '':
        attach_filepath = input_filepath
        # 读取附件文件
        attach_file = open(attach_filepath, 'rb')
        attach_part = MIMEApplication(attach_file.read(), Name=os.path.basename(attach_filepath))
        attach_part['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(attach_filepath)
        attach_file.close()
        # 将附件放到邮件中
        message.attach(attach_part)


    try:
        # 连接SMTP服务器
        print 'connecting ...'
        smtp = smtplib.SMTP_SSL()
        smtp.connect(smtp_server)

        # 登陆发件人的账户
        print 'loginning ...'
        smtp.login(sender, sender_pwd)

        # 开始发送邮件
        print 'sending ...'
        smtp.sendmail(sender, receivers, message.as_string())

        # 结束后关闭与服务器的连接
        smtp.close()
        print 'seccuss!'
    except Exception, e:
        print e


if __name__ == '__main__':
    main()



