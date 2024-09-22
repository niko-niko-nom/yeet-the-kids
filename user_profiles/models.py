from django.db import models

class UserProfile(models.Model):
    GENDERS = [
        ('geheim', 'Geheim'),
        ('vrouw', 'Vrouwelijk'),
        ('man', 'Mannelijk'),
        ('nb', 'Non-Binair'),
    ]

    ROLES = {
        'ceo': 'Chief Executive Officer',
        'cco': 'Chief Cheese Officer',
        'kaaskop': 'Kaaskop',
        'kaastester': 'Kaastester',
        'dev': 'Developer',
        'master': 'SCRUM Master',
        'owner': 'Product Owner',
        'caf': 'Cafetariamedewerker',
    }

    # Profile picture
    pfp = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    # Name and basic info
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDERS)
    pronouns = models.CharField(max_length=15, blank=True)
    number = models.CharField(max_length=12)
    email = models.EmailField(max_length=75)

    # Boolean fields for roles
    ceo = models.BooleanField(default=False)
    cco = models.BooleanField(default=False)
    kaaskop = models.BooleanField(default=True)
    kaastester = models.BooleanField(default=False)
    dev = models.BooleanField(default=False)
    master = models.BooleanField(default=False)
    owner = models.BooleanField(default=False)
    caf = models.BooleanField(default=False)
    
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
    