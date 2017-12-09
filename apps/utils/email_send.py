from random import Random
from django.core.mail import send_mail
from users.models import EmailVerifyRecord
from online.settings import EMAIL_FROM


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_code_email(email, send_type="register"):
    code = random_str(8)
    email_record = EmailVerifyRecord()
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == "register":
        email_title = "注册激活链接"
        email_body = "请点击下面的链接激活你的账号: http://127.0.0.1:8001/active/{0}".format(code)
    elif send_type == "forget":
        email_title = "注册密码重置链接"
        email_body = "请点击下面的链接重置密码: http://127.0.0.1:8001/reset/?code={0}".format(code)
    elif send_type == "update_email":
        email_title = "邮箱修改验证码"
        email_body = "你的邮箱验证码为: {0}".format(code)

    send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
    if not send_status:
        print("邮件发送失败")
