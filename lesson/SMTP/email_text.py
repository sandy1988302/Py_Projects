import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
# 成功开启IMAP/SMTP服务，在第三方客户端登录时，登录密码输入以下授权密码:YZYISBALZTLFYFWU
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "chenhao19880909@163.com"  # 用户名
mail_pass = "YZYISBALZTLFYFWU"  # 授权密码

sender = 'chenhao19880909@163.com'
receivers = ['290591844@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('你们这帮叛军,给我老实呆着。看我派坦克来把你们一个个送上天！', 'plain', 'utf-8')
message['From'] = Header("首都警备司令部张泰玩", 'utf-8')
message['To'] = Header("保安司令部全斗焕", 'utf-8')

subject = '反叛者，老实！逐一发送战车！'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
