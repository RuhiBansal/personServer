from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200,unique=True)
    birthYear = models.IntegerField()
    deathYear = models.IntegerField()
    deathYear=models.IntegerField()
