from django import forms

class UserData(forms.Form):
    GENDERS = [
        ('geheim', 'Geheim'),
        ('vrouw', 'Vrouwelijk'),
        ('man', 'Mannelijk'),
        ('nb', 'Non-Binair'),
    ]

    ROLES = [
        ('ceo', 'Chief Executive Officer'),
        ('cco', 'Chief Cheese Officer'),
        ('kaaskop', 'Kaaskop'),
        ('kaastester', 'Kaastester'),
        ('dev', 'Developer'),
        ('master', 'SCRUM Master'),
        ('owner', 'Product Owner'),
        ('caf', 'Cafetaria Medewerker'),
    ]

    name = forms.CharField(label="Uw naam:", max_length=100)
    age = forms.DateField(label="Uw geboortedag:")
    city = forms.CharField(label="Uw woonplaats:", max_length=100)
    gender = forms.ChoiceField(label="Uw geslacht:", choices=GENDERS)
    pronouns = forms.CharField(label="Uw voornaamwoorden:", max_length=15)
    number = forms.CharField(label="Uw mobiele nummer:", max_length=12)
    email = forms.EmailField(label="Uw e-mailadres:", max_length=75)
    roles = forms.MultipleChoiceField(label="Uw rollen:", choices=ROLES)
    bio = forms.CharField(label="Uw biografie:", max_length=1000)
    trivia1 = forms.CharField(label="Een leuk feitje over u:", max_length=100)
    trivia2 = forms.CharField(label="Nog een leuk feitje over u:", max_length=100)
    trivia3 = forms.CharField(label="Een ander leuk feitje over u:", max_length=100)
    trivia4 = forms.CharField(label="Een nog leuker feitje over u:", max_length=100)
    trivia5 = forms.CharField(label="Een oorverdoverend leuk feitje over u:", max_length=100)