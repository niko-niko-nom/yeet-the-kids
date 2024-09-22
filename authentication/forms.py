from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(
            min_length=6,
            max_length=128,
            required=True,
            widget=forms.PasswordInput()
        )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'miku@kaasinc.moe'
        self.fields['password'].widget.attrs['placeholder'] = 'omg pipebomb, so coooool'
