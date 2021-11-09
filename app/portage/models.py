from django.db import models


class Portage(models.Model):
    driver_name = models.CharField(max_length=200)
    car_name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    car_color = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)




