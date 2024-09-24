from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from . import models
from . import forms

# Create your views here.
class RoleListView(View):
    def get(self, request):
        roles = models.Roles.objects.all()
        return HttpResponse('kaas')
    
class RolesView(View):
    def get(self, request, id):
        role = models.Roles.objects.get(id=id)
        return HttpResponse('kaas')

class CreateRoles(View):
    def get(self, request,):
        form = forms.Editform()
        return HttpResponse('kaas')
    
    def post(self, request):
        form = forms.Editform(request.POST)

        if not form.is_valid():
            return HttpResponse('kaas')