from django import forms
from .models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name']


class User(forms.Form):
    GENDERS = [
        ('geheim', 'Geheim'),
        ('vrouw', 'Vrouwelijk'),
        ('man', 'Mannelijk'),
        ('nb', 'Non-Binair'),
    ]
    
    # pfp = forms.ImageField(widget=forms.FileInput(attrs={
    #     'class': 'form-control',
    #     'accept': 'image/*'
    # }))
    
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your name'
    }))
    
    email = forms.EmailField(max_length=75, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email'
    }))
    
    birthday = forms.DateField(widget=forms.DateInput(attrs={
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
