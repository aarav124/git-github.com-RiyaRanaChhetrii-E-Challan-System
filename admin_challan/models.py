from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Challan(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    license = models.IntegerField()
    challan_num = models.IntegerField()
    vehicle_type = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.name
 