from django.views import View
from django.shortcuts import render, HttpResponse

class LoginView(View):
    def get(self, request):
        return render(request, "inlog.html")

    def post(self, request):
        return HttpResponse("You did a post!")

