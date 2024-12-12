import random

from celery import shared_task
from time import sleep

from django.core.mail import send_mail
from accounts.models import User
from main.models import Car, CarBrand, CarColor, Category


@shared_task
def send_email():
    send_mail('Test mail', 'this is a test email',
              'qoshqulovshahzod9@gmail.com', ['qoshqulovshahzod9@gmail.com'], fail_silently=False)
    return 1


@shared_task
def create_cars(amount=100):
    car_brand = CarBrand.objects.create(name='Xiaomi')
    red = CarColor.objects.create(name='Red')
    black = CarColor.objects.create(name='Black')
    white = CarColor.objects.create(name='White')
    category1 = Category.objects.get(id=1)
    category2 = Category.objects.get(id=2)
    user = User.objects.get(id=1)
    for i in range(amount):
        color = random.choice([red, black, white])
        category = random.choice([category1, category2])
        price = random.randint(100000000, 1000000000)
        Car.objects.create(
            name=f"Car {i}",
            user=user,
            produced_year='2024-12-12',
            color=color,
            price=price,
            case='Sedan',
            location='Tashkent',
            brand=car_brand,
            fuel='Benzin',
            category=category)
    return 'Cars created successfuly!'


@shared_task
def longtime_add(x, y):
    sleep(10)
    return x + y
