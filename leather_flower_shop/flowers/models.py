"""
    Importing module model from django framework
"""
from django.db import models


class FlowerOrder(models.Model):
    """
        This class describe flower model
    """
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
