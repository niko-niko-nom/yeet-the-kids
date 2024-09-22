from django import forms

class UserData(forms.Form):
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
    
    pfp = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control',
        'accept': 'image/*'
    }))
    
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your name'
    }))
    
    age = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date'
    }))
    
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your city'
    }))
    
    gender = forms.ChoiceField(choices=GENDERS, widget=forms.Select(attrs={
        'class': 'form-select'
    }))
    
    pronouns = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your pronouns'
    }))
    
    number = forms.CharField(max_length=12, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your phone number'
    }))
    
    email = forms.EmailField(max_length=75, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email'
    }))
    
    # Boolean fields for each role
    ceo = forms.BooleanField(required=False, label=ROLES['ceo'], widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }))
    cco = forms.BooleanField(required=False, label=ROLES['cco'], widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }))
    kaaskop = forms.BooleanField(required=False, label=ROLES['kaaskop'], widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }))
    kaastester = forms.BooleanField(required=False, label=ROLES['kaastester'], widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }))
    dev = forms.BooleanField(required=False, label=ROLES['dev'], widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }))
    master = forms.BooleanField(required=False, label=ROLES['master'], widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }))
    owner = forms.BooleanField(required=False, label=ROLES['owner'], widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }))
    caf = forms.BooleanField(required=False, label=ROLES['caf'], widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }))
    
    bio = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5,
        'placeholder': 'Tell us about yourself'
    }))
    
    trivia1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Fun fact 1'
    }))
    
    trivia2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Fun fact 2'
    }))
    
    trivia3 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Fun fact 3'
    }))
    
    trivia4 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Fun fact 4'
    }))
    
    trivia5 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Fun fact 5'
    }))
