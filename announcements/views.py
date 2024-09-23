from django.shortcuts import render,HttpResponse
from django.views import View

class AnnouncementListView(View):
    def get(request):
        return HttpResponse("oui oui baguette")

class AnnouncementView(View):
    def get(request):
        pass
        
