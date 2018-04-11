import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

_user = "mrbai1995@126.com"
_pwd = "baixin1995"
_to = "1424530412@qq.com"
to_list=["1424530412@qq.com"]
# 如名字所示Multipart就是分多个部分
msg = MIMEMultipart()
msg["Subject"] = "小猪在哪里"
msg["From"] = _user
# msg["To"] = ";".join(to_list)
msg["To"] =_to
# ---这是文字部分---
part = MIMEText("小猪小猪~，啥时候撤，哈哈，我用python测试下")
msg.attach(part)
#mp3类型附件
part = MIMEApplication(open('蜗牛-周杰伦.mp3','rb').read())
part.add_header('Content-Disposition', 'attachment', filename="蜗牛-周杰伦.mp3")
msg.attach(part)
#jpg类型附件
part = MIMEApplication(open('dog.jpg','rb').read())
part.add_header('Content-Disposition', 'attachment', filename="dog.jpg")
msg.attach(part)

s = smtplib.SMTP("smtp.126.com", timeout=30)  # 连接smtp邮件服务器,端口默认是25
s.login(_user, _pwd)  # 登陆服务器
s.sendmail(_user, _to, msg.as_string())  # 发送邮件
s.close()