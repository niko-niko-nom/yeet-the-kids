from django.db import models

# Create your models here.

class Vote(models.Model):
    ip = models.CharField(max_length=15, unique=True)
    vote = models.IntegerField()
