from django.core.mail import send_mail
from send_email.celeryapp import app

from .service import send
from .models import Contact


@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'Вы подписались на рассылку',
            'Мы будем присылать Вам много спама каждые 10 минут.',
            'https://is.gd/yOWGcT',
            [contact.email],
            fail_silently=False,
        )
