from django.core.mail import EmailMessage
from .models import User, OneTimePassword
from config.settings.base import DEFAULT_FROM_EMAIL
import random


def generateOtp():
    otp = ""
    for i in range(6):
        otp += str(random.randint(1, 9))
    return otp


def send_code_to_user(emai):
    Subject = "Bir martalik kod Emailni tasdiqlash uchun"
    otp_code = generateOtp()
    print(otp_code)
    user = User.objects.get(emai=emai)
    current_site = "conf.com"
    email_body = f"{current_site}site {otp_code} code"
    from_email =DEFAULT_FROM_EMAIL

    OneTimePassword.objects.create(user=user, code=otp_code)

    send_mail=EmailMessage(subject=Subject, body=email_body, from_emai=from_email, to=[emai])
    send_mail.send(fail_silently=True)
