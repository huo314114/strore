import zmail
# 你的邮件内容
mail_content = {
    'subject': 'Success!',  # 随便填写
    'content_text': '！',  # 随便填写
    'attachments': ['E:\\python\\pythonday1\\邮件\\计算器.html'],
}

# 使用你的邮件账户名和密码登录服务器
server = zmail.server('1512356058@qq.com', 'uxefeggkhzptfjci')
# 发送邮件
server.send_mail('2687726791@qq.com',mail_content )