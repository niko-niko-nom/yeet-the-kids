from django.shortcuts import render, HttpResponse
from announcements.models import Announcement
from django.contrib.auth.decorators import login_required
from user_profiles.models import User

# Create your views here.

@login_required
def home(request):
    announcements = Announcement.objects.order_by("-id")[:3]
    profiles = User.objects.all()   
    return render(request, "dashboard.html", { 'announcements': announcements, 'profiles': profiles })

@login_required
def hboict(request):
    return render(request, "hboict.html")

@login_required
def scrum(request):
    return render(request, "scrum.html")
