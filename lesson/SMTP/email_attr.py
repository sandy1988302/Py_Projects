import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication

# 第三方 SMTP 服务
# 成功开启IMAP/SMTP服务，在第三方客户端登录时，登录密码输入以下授权密码:（163）YZYISBALZTLFYFWU（QQ）inukdsuhfhqybhjh
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "290591844@qq.com"  # 用户名
mail_pass = "inukdsuhfhqybhjh"  # 授权密码

sender = '290591844@qq.com'
receivers = ['chenhao19880909@163.com', 'sandy1988302@foxmail.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header("保安司全斗焕司令官")
msgRoot['To'] = Header("主送陆军参谋总长全国戒严司令官郑升和")
msgRoot['Cc'] = Header("抄送首都警备司张泰玩司令官")
subject = '西冰库大酒店专用邮件标题'
msgRoot['Subject'] = Header(subject, 'utf-8')
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)
mail_msg = """
<p>招待券，请收</p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
# 附件1，解决中文乱码
attach_file = '肃反名单.txt'
att1 = MIMEApplication(open('肃反名单.txt', 'rb').read())
att1["Content-Type"] = 'application/octet-stream'
att1.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', attach_file))
msgRoot.attach(att1)

# 构造附件2
att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="t2.txt"'
msgRoot.attach(att2)

smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
smtpObj.login(mail_user, mail_pass)
smtpObj.sendmail(sender, receivers, msgRoot.as_string())
print("邮件发送成功")
