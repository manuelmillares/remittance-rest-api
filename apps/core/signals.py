from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.core import models
import requests


@receiver(post_save, sender=models.Remittance)
def send_telegram_message(sender, instance, created, **kwargs):
    if created:
        bot_message = 'Nueva Remesa Creada'
        bot_token = '1162727727:AAGCUBJ_yE5CegDYOHeczxB7M11o_aCJz0A'
        bot_chatID = '645960852'
        send_text = 'https://api.telegram.org/bot' + bot_token + \
            '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

        response = requests.get(send_text)
