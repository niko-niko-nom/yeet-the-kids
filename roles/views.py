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
    
    def post(self, request, id):
        models.Roles.objects.filter(id=id).delete()
        return redirect("roles")
    
class EditRole(View):
    def get(self, request, id):
        role = models.Roles.objects.get(id=id)
        form = forms.Editform(initial={"title" : role.title, "text": role.text})
        return render(request, "edit_roles.html", {'form':form,})

    def post(self, request, id):
        form = forms.Editform(request.POST)

        if not form.is_valid():
            return render(request, "edit_roles.html", {'form':form})
        role = models.Roles.objects.get(id=id)
        role.title = form.cleaned_data['title']
        role.text = form.cleaned_data['text']
        role.save()
        return redirect('role', id=role.id)

class CreateRoles(View):
    def get(self, request,):
        form = forms.Editform()
        return render(request, "edit_roles.html", {'form':form})
    
    def post(self, request):
        form = forms.Editform(request.POST)

        print("hallo")

        if not form.is_valid():
            print("o jee")
            return render(request, "edit_roles.html", {'form':form})

        print("hallo 1")
        
        role = models.Roles(title=form.cleaned_data["title"], text=form.cleaned_data["text"])
        role.save()

        return redirect("role", id=role.id)