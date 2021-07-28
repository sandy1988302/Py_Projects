import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
# 成功开启IMAP/SMTP服务，在第三方客户端登录时，登录密码输入以下授权密码:（163）YZYISBALZTLFYFWU（QQ）inukdsuhfhqybhjh
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "290591844@qq.com"  # 用户名
mail_pass = "inukdsuhfhqybhjh"  # 授权密码

sender = '290591844@qq.com'
receivers = ['chenhao19880909@163.com', 'sandy1988302@foxmail.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header("保安司令部全斗焕小将")
msgRoot['To'] = Header("主送陆军总参谋长郑升和上将")
msgRoot['Cc'] = Header("抄送代理总统崔圭夏")
subject = '保安司专用邮件标题'
msgRoot['Subject'] = Header(subject, 'utf-8')
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)
mail_msg = """
<p>禁止外传！</p>
<p><a href="https://www.163.com/">极密，阅后即焚</a></p>
<p>像什么话，这说的都是什么话</p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
# 构造附件1
att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["attachment"] = 'attachment'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字,注意中文有附件编码问题，会出现tcmime.*.bin
name = '肃反名单.txt'.encode("utf-8")
print(name)
att1["Content-Disposition"] = 'attachment; filename=%s' % name
msgRoot.attach(att1)
# 构造附件2
att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
msgRoot.attach(att2)
# 指定图片为当前目录
fp = open('PIC/像什么话，这说的都是什么话.jpg', 'rb')
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
