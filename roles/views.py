from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from . import models
from . import forms

# Create your views here.
class RoleListView(View):
    def get(self, request):
        roles = models.Roles.objects.all()
        return render(request, "roles.html", {'roles':roles})
    
class RolesView(View):
    def get(self, request, id):
        role = models.Roles.objects.get(id=id)
        return render(request, "view_roles.html", {'role':role})

class CreateRoles(View):
    def get(self, request,):
        form = forms.Editform()
        return render(request, "edit_announcements.html", {'form':form})
    
    def post(self, request):
        form = forms.Editform(request.POST)

        if not form.is_valid():
            return render(request, "edit_roles.html", {'form':form})