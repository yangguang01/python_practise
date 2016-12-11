#! /usr/bin/env python
#coding=utf-8

import smtplib
import os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def main():

	sender = 'yangg062@gmail.com'
	sender_pwd = 'icfzdkqrxlggfecz'
	smtp_server = 'smtp.gmail.com'

	receivers = ['745593336@qq.com']

	message = MIMEMultipart()
	message['Subject'] = 'the tittle'
	message['From'] = sender
	message['To'] = ''
	message['Cc'] = ''
	message['Bcc'] = ''

	mail_body = '''
hi all:

	Hello email

	'''

	#讲正文放到邮件结构里
	message.attach(MIMEText(mail_body, 'plain', 'utf-8'))

	try:
		# 连接SMTP服务器
		smtp = smtplib.SMTP_SSL()
		smtp.connect(smtp_server)

		#登陆发件人的账户
		smtp.login(sender, sender_pwd)

		#开始发送邮件
		smtp.sendmail(sender, receivers, message.as_string())

		#结束后关闭与服务器的连接
		smtp.close()
	except Exception, e:
		print e


if __name__ == '__main__':

	main()



