#-*- coding: utf-8 -*-
# Send customized message
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import smtplib
import time

class Message:
    def __init__(self, subject, sendFrom, sendTo, body, photo=None):
        "Initialization"
        self.msg = MIMEMultipart('related')
        self.msg['Subject'] = subject
        self.msg['From'] = sendFrom
        self.sendTo = sendTo
        self.msg['To'] = ";".join(sendTo)
        self.msg["Accept-Language"] = 'zh-CN'
        self.msg["Accept-Charset"] = 'ISO-8859-1,utf-8'
        self.msgAlt = MIMEMultipart('alternative')
        self.msg.attach(self.msgAlt)
        
        self.msgAlt.attach(MIMEText('Plain Text'))
        self.msgAlt.attach(MIMEText(body, 'html', 'utf-8'))

        if photo:
            f = open(photo, 'rb')
            msgImg = MIMEImage(f.read())
            f.close()

            msgImg.add_header('Content-ID', '<image1>')
            self.msg.attach(msgImg)
    def sendMail(self):
        smtp = smtplib.SMTP_SSL('smtp.xxx.com', 465)
        smtp.login('xxx@xxx.com', 'xxxxxx')
        smtp.sendmail(self.msg['From'], self.sendTo, self.msg.as_string())
        smtp.quit()
        print "Sent"

if __name__ == '__main__':
    import NGPOD
    photo = NGPOD.NGPOD()
    photo.getPage()
    photo.getImage('./Images/')
    photo.getImageInfo()

    body = ''
    body += '<p>Hi!</p>'
    body += '<p>Test Test Test</p>'
    body += '<br><br>'
    body += '<h1>Picture of the Day</h1>'
    body += '<br><br>'
    body += '<img src="cid:image1" width="495" height="371"><br>'
    body += '<h2>' + photo.imageCaption + '</h2>'
    body += '<p><i>' + photo.imageNote + '</i></p>'
    body += '<p>Test Test Test</p>'
    body += '<p>====================<p>'
    body += '<br>测试中文<br>'
    body += '<br>测试英文<br>'
    body += '<p>====================<p>'
    body += '<p>Test Test Test Test Test Test</p>'
    msg = Message('Test New', 'xxx@xxx.xxx', ['xxx@xxx.xxx', 'xxx@xxx.xxx'], body, photo.imagePath)
    msg.sendMail()
