from django.shortcuts import render
from django.views import View

# Create your views here.

class AnnouncementListView(View):
    def get(request):
        
