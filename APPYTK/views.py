from django.shortcuts import render, HttpResponse
from announcements.models import Announcement
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    announcements = Announcement.objects.order_by("-id")[:3]
    return render(request, "dashboard.html", { 'announcements': announcements })

@login_required
def hboict(request):
    announcements = Announcement.objects.order_by("-id")[:3]
    return render(request, "hboict.html")
