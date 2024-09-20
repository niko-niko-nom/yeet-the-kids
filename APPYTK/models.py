from django.db import models

class User(models.Model):
    name = models.CharField(max_length=24)
    password = models.CharField(max_length=100)
    permissions = models.IntegerField()
