from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Вы подписаны на рассылку',
        'Мы будем присылать вам много спама',
        'https://is.gd/yOWGcT',
        [user_email],
        fail_silently=False,
    )
