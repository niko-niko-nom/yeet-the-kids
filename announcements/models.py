from django.db import models

# Create your models here.
class Announcements(models.Model)
    title = models.CharField(max_length=32)
    text = models.TextField()

    