from django.db import models

# Create your models here.
class places(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    city = models.CharField(max_length=100)