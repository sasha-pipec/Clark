import random

from django.core.mail import send_mail

from conf.settings.django import EMAIL_HOST_USER

TITLE = 'Корпоративный чат Clark'
BODY = 'Ваш код для подтверждения регистрации: '


def generate_code():
    digits = [str(random.randint(0, 9)) for _ in range(5)]
    return ''.join(digits)


def confirm_registration(client_email):
    confirmation_code = generate_code()
    send_mail(
        TITLE,
        BODY + confirmation_code,
        EMAIL_HOST_USER,
        [client_email, ],
    )
    return confirmation_code
