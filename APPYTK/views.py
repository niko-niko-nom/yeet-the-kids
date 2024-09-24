from django.shortcuts import render, HttpResponse
from announcements.models import Announcement

# Create your views here.

def home(request):
    announcements = Announcement.objects.order_by("-id")[:3]
    return render(request, "dashboard.html", { 'announcements': announcements })
