from django.db import models
from django.urls import reverse


class Phone(models.Model):
    image = models.ImageField(upload_to='phones-images/', null=True)
    name = models.CharField(max_length=255)
    series = models.CharField(max_length=255)
    screen_diagonal = models.FloatField()
    display_resolution = models.CharField(max_length=255)
    type_of_matrix = models.CharField(max_length=255)
    screen_refresh_rate = models.PositiveIntegerField()
    count_of_sim_cards = models.PositiveSmallIntegerField()
    ram = models.PositiveIntegerField()
    built_in_memory = models.IntegerField()
    operating_system = models.CharField(max_length=255)
    count_of_cores = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    width = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    depth = models.CharField(max_length=255)
    guarantee = models.IntegerField()
    country_of_manufacture = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефони'


class Order(models.Model):
    product = models.ForeignKey(Phone, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return f'Замовлення {self.id} - {self.product.name}'

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'