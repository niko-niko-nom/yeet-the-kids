from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from . import models

# Create your views here.
class RoleListView(View):
    def get(self, request):
        roles = models.Roles.objects.all()
        return HttpResponse('nigga')
    
class RolesView(View):
    def get(self, request, id):
        role = models.Roles.objects.get(id=id)
        return HttpResponse('nigga2')