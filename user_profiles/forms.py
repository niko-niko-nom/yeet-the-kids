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

    pfp = forms.ImageField(label="Uw profielfoto:", type="file", accept="image/*", value="{{current_pfp}}")
    name = forms.CharField(label="Uw naam:", max_length=100, value="{{current_name}}")
    age = forms.DateField(label="Uw geboortedag:", value="{{current_dob}}")
    city = forms.CharField(label="Uw woonplaats:", max_length=100, value="{{current_city}}")
    gender = forms.ChoiceField(label="Uw geslacht:", choices=GENDERS, value="{{current_gender}}")
    pronouns = forms.CharField(label="Uw voornaamwoorden:", max_length=15, value="{{current_pronouns}}")
    number = forms.CharField(label="Uw mobiele nummer:", max_length=12, value="{{current_number}}")
    email = forms.EmailField(label="Uw e-mailadres:", max_length=75, value="{{current_email}}")
    roles = forms.MultipleChoiceField(label="Uw rollen:", choices=ROLES, value="{{current_roles}}")
    bio = forms.CharField(label="Uw biografie:", max_length=1000, value="{{current_bio}}")
    trivia1 = forms.CharField(label="Een leuk feitje over u:", max_length=100, value="{{current_trivia1}}")
    trivia2 = forms.CharField(label="Nog een leuk feitje over u:", max_length=100, value="{{current_trivia2}}")
    trivia3 = forms.CharField(label="Een ander leuk feitje over u:", max_length=100, value="{{current_trivia3}}")
    trivia4 = forms.CharField(label="Een nog leuker feitje over u:", max_length=100, value="{{current_trivia4}}")
    trivia5 = forms.CharField(label="Een oorverdoverend leuk feitje over u:", max_length=100, value="{{current_trivia5}}")