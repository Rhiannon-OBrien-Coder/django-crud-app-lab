from django.db import models
from django.urls import reverse

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    rating = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('coffee-detail', kwargs={'coffee_id': self.id})