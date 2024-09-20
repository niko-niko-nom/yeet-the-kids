from django.views import View
from django.shortcuts import render, HttpResponse
from ..forms import LoginForm

class LoginView(View):
    def get(self, request):
        return render(request, "inlog.html", { 'form': LoginForm() })

    def post(self, request):
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, "inlog.html", { 'form': form })

        print(form.cleaned_data)
        return HttpResponse("You did a post!")

