import requests
from django.dispatch import receiver
from django.db.models.signals import post_save
from books.models import Sale
from books.models import Product

TELEGRAM_TOKEN = "7355857174:AAHcjHeIJ_k6EQ19UTjx2idofAyNIsmygqo"
CHAT_ID = "963020731"


@receiver(post_save, sender=Sale)
def check_product_quantity(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        if product.quantity < 10:
            text = f"Warning: Product '{product.name}' has less than 10 items left in stock! Current quantity: {product.quantity}"
            send_telegram_message(text)


def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    params = {
        'chat_id': CHAT_ID,
        'text': text
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Failed to send message: {response.text}")

