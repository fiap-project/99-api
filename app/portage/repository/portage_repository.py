from pprint import pprint
from django.db import models
from portage.models import *


class PortageRepository():
    def search_nearby_drivers(latitude, longitude, car_type):
        pprint(longitude)
        for p in models.Portage.objects.raw("""SELECT *
                                        FROM
                                          (SELECT *,
                                                  (3959 * acos(cos(radians(6.414478)) * cos(radians({lat})) * cos(radians({lng}) - radians(12.466646)) + sin(radians(6.414478)) * sin(radians({lat})))) AS distance
                                           FROM station_location) al
                                        WHERE distance < 25 AND car_type = "{cartype}"
                                          ORDER
                                                BY distance
                                        LIMIT 20;""".format(lat=latitude, lng=longitude), cartype=car_type):
            return p
