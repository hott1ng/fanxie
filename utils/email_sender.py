# -*- coding: utf-8 -*-
from email.utils import formataddr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def sender(event, pic_path=None,text=None):
    sender = '963454524@qq.com'
    receivers = '963454524@qq.com'
    message = MIMEMultipart('related')
    message['Subject'] = event
    message['From'] = formataddr(("帆蝎", sender))
    message['To'] = receivers
    if pic_path:
        content = MIMEText('<html><body><img src="cid:imageid" alt="imageid"></body></html>', 'html', 'utf-8')
        message.attach(content)

        with open(pic_path, "rb") as f:
            img_data = f.read()

        img = MIMEImage(img_data)
        img.add_header('Content-ID', 'imageid')
        message.attach(img)
    else:
        content = MIMEText(text, 'plain', 'utf-8')
        message.attach(content)

    try:
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(sender, "yfkfqulvztelbbfi")
        server.sendmail(sender, receivers, message.as_string())
        server.quit()
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)


if __name__ == '__main__':
    sender('寄养', r'log/screenshot/1.png')
