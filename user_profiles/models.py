from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDERS = [
        ('geheim', 'Geheim'),
        ('vrouw', 'Vrouwelijk'),
        ('man', 'Mannelijk'),
        ('nb', 'Non-Binair'),
    ]

    # Profile picture
    pfp = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    # Name and basic info
    city = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDERS)
    pronouns = models.CharField(max_length=15, blank=True)
    number = models.CharField(max_length=12)

    # Biography
    bio = models.TextField(max_length=1000, blank=True)

    # Trivia fields
    trivia1 = models.CharField(max_length=100, blank=True)
    trivia2 = models.CharField(max_length=100, blank=True)
    trivia3 = models.CharField(max_length=100, blank=True)
    trivia4 = models.CharField(max_length=100, blank=True)
    trivia5 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name