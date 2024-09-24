from django import forms
class Editform(forms.Form):
    title = forms.CharField(max_length=32)
    text = forms.CharField(min_length=2, widget=forms.Textarea)
