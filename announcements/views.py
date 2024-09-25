from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from . import models
from . import forms

class AnnouncementListView(View):
    @login_required
    def get(self, request):
        announcements = models.Announcement.objects.all()
        return render(request, "announcements.html", {'announcements':announcements})

class AnnouncementView(View):
    @login_required
    def get(self, request, id): 
        announcement = models.Announcement.objects.get(id=id)
        return render(request, "view_announcements.html", {'announcement':announcement})
   
    @login_required
    def post(seld, request, id):
        models.Announcement.objects.filter(id=id).delete()
        return redirect("announcements")
        
    
class EditAnnouncement(View):
    @login_required
    def get(self, request, id):
        announcement = models.Announcement.objects.get(id=id)
        form = forms.Editform(initial={"title": announcement.title, "text": announcement.text})
        return render(request, "edit_announcements.html", {'form':form, 'announcement': announcement})
    @login_required
    def post(self, request, id):
        form = forms.Editform(request.POST)

        if not form.is_valid():
            return render(request, "edit_announcements.html", {'form':form})
        announcement = models.Announcement.objects.get(id=id)
        announcement.title = form.cleaned_data['title']
        announcement.text = form.cleaned_data['text']
        announcement.save()
        return redirect('announcement', id=announcement.id)
        
class CreateAnnouncement(View):
    @login_required
    def get(self, request):
        form = forms.Editform()
        return render(request, "edit_announcements.html", {'form':form})

    @login_required
    def post(self, request):
        form = forms.Editform(request.POST)

        if not form.is_valid():
            return render(request, "edit_announcements.html", {'form':form})
        
        announcement = models.Announcement(title=form.cleaned_data["title"], text=form.cleaned_data["text"])
        announcement.save()

        return redirect("announcement", id=announcement.id)
        
