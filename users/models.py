from django.db import models

# Create your models here.

class Usersdata(models.Model):

    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=200)
    children = models.CharField(max_length=200)
