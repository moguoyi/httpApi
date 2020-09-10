#coding:utf-8
import smtplib
from email.mime.text import MIMEText
class SendEmail:
    global send_user
    global email_host
    global password
    password="mgy543622257"
    email_host = "smtp.163.com"
    send_user = "18513827507@163.com"
    def send_email(self,user_list,sub,content):
        user = "莫忆"+"<"+send_user+">"
        message = MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub
        message['From'] = send_user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        server.close()

if __name__=="__main__":
    sen = SendEmail()
    user_list = ['543622257@qq.com']
    sub = "这个是测试邮件"
    content = "这是测试邮件内容"
    sen.send_email(user_list,sub,content)

