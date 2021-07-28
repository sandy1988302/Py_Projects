import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方 SMTP 服务
# 成功开启IMAP/SMTP服务，在第三方客户端登录时，登录密码输入以下授权密码:（163）YZYISBALZTLFYFWU（QQ）inukdsuhfhqybhjh
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "290591844@qq.com"  # 用户名
mail_pass = "inukdsuhfhqybhjh"  # 授权密码
sender = '290591844@qq.com'
receivers = ['chenhao19880909@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("首都警备司令部张泰玩")
message['To'] = Header("chenhao19880909@163.com")
subject = 'Python SMTP 邮件'
message['Subject'] = Header(subject, 'utf-8')
# 邮件正文内容
message.attach(MIMEText('这是菜鸟教程Python 邮件发送……', 'plain', 'utf-8'))
# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)
# 构造附件2，传送当前目录下的 runoob.txt 文件
att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
message.attach(att2)
smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
smtpObj.login(mail_user, mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
print("邮件发送成功")
