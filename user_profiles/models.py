from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

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
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    birthday = models.DateField(default=datetime.datetime.now())
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

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)
    
