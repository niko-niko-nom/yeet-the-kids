from django.shortcuts import render,HttpResponse
from django.views import View
from . import models

class AnnouncementListView(View):
    def get(self, request):
        announcements = models.Announcement.objects.all()
        return render(request, "announcements.html", {'announcements':announcements})

class AnnouncementView(View):
    def get(self, request, id):
        return HttpResponse("oui oui baguette")
        
