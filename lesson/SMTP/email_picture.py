import smtplib
import os
from email.mime.image import MIMEImage
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
msgRoot['From'] = Header("首都警备司张泰玩司令官")
msgRoot['To'] = Header("主送保安司全斗焕司令官")
msgRoot['Cc'] = Header("抄送代理总统崔圭夏")
subject = '保安司专用邮件标题'
msgRoot['Subject'] = Header(subject, 'utf-8')
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)
mail_msg = """
<p>战车警告！</p>
<p><a href="https://www.163.com/">极密，阅后即焚</a></p>
<p>怎么到头来都是我背锅</p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
# 构造附件1
att1 = MIMEApplication(open('肃反名单.txt', 'rb').read())
att1["Content-Type"] = 'application/octet-stream'
name = '肃反名单.txt'
mail_coding = 'utf-8'
att_header = Header(os.path.basename(name), mail_coding)
print(att_header)
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="%s"' % att_header
att1["Content-Disposition"] = "attachment; filename*=utf-8'''肃反名单.txt'"
msgRoot.attach(att1)

# 构造附件2
att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="a.txt"'
msgRoot.attach(att2)
# 指定图片为当前目录
fp = open('PIC/怎么到头来都是我背锅.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)
smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
smtpObj.login(mail_user, mail_pass)
smtpObj.sendmail(sender, receivers, msgRoot.as_string())
print("邮件发送成功")
