import smtplib
from email.mime.text import MIMEText
import email.utils
to_list=["13040283313@163.com", "627283764@qq.com"]
#对于大型的邮件服务器，有反垃圾邮件的功能，必须登录后才能发邮件，如126,163
mail_server="smtp.126.com"         # 126的邮件服务器
mail_user="mrbai1995@126.com"   #必须是真实存在的用户，这里我测试的时候写了自己的126邮箱
mail_pass="19950725bx"               #必须是对应上面用户的正确密码，我126邮箱对应的密码

def send_mail(to_list,sub,content):
    '''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@126.com","sub","content")
    '''
    me=mail_user+"<"+mail_user+">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_server)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except smtplib.SMTPException:
        # print("Falied")
        return False
if __name__ == '__main__':
    if send_mail(to_list,"subject","content"):
        print ("发送成功")
    else:
        print("Falied")