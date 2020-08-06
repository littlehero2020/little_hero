from django.conf import settings
from django.db import models
from django.utils import timezone


class CitiesTable(models.Model):
    city = models.CharField(max_length=30, default='')
    gu = models.CharField(max_length=40, default='')

    def publish(self):
        self.save()
    
    def __str__(self):
        return self.gu

class Cities(models.Model):
    city = models.CharField(max_length=30)

    def publish(self):
        self.save()
    
    def __str__(self):
        return self.city