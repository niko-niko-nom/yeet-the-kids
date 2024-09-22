from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from . import forms

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')

        return render(request, "inlog.html", { 'form': forms.LoginForm() })

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('/')

        form = forms.LoginForm(request.POST)
        if not form.is_valid():
            return render(request, "inlog.html", { 'form': form })

        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        # we use username here because of a custom auth backend
        user = authenticate(request, username=email, password=password)
         
        print(email)
        print(password)
        print(user)

        if user is None:
            print("Failed login request")
            return render(request, "inlog.html", { 'form': form, 'error': 'No user found' })

        login(request, user)
        print("Login request succeeded for " + user.get_username())
        return redirect("/")

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect("login")
