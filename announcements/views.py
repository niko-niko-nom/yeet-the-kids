from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from . import models
from . import forms

class AnnouncementListView(View):
    def get(self, request):
        announcements = models.Announcement.objects.all()
        return render(request, "announcements.html", {'announcements':announcements})

class AnnouncementView(View):
    def get(self, request, id):
        announcement = models.Announcement.objects.get(id=id)
        return render(request, "view_announcements.html", {'announcement':announcement})
    
class CreateAnnouncement(View):
    def get(self, request):
        form = forms.Editform()
        return render(request, "edit_announcements.html", {'form':form})

    def post(self, request):
        form = forms.Editform(request.POST)

        if not form.is_valid():
            return render(request, "edit_announcements.html", {'form':form})
        
        announcement = models.Announcement(title=form.cleaned_data["title"], text=form.cleaned_data["text"])
        announcement.save()

        return redirect("announcement", id=announcement.id)
        
