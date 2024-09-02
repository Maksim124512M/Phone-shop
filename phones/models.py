from django.db import models


class Phone(models.Model):
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
