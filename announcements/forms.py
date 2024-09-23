from django import forms
class Editform(forms.Form):
    title = forms.CharField(max_length=32)
    text = forms.Textarea()