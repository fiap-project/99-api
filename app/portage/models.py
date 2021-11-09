from django.db import models


class Portage(models.Model):
    driver_name = models.CharField(max_length=200)
    car_name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    car_color = models.CharField(max_length=100)
    car_license_plate = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    long = models.CharField(max_length=100)




