from django.urls import path
from . import views
from . import models
from . import forms

urlpatterns = [
    path("", views.RoleListView.as_view(), name='roles'),
    path("<int:id>/", views.RolesView.as_view(), name='role'),
    path("new/", views.CreateRoles.as_view(), name='new role'),
    path("<int:id>/edit/", views.EditRole.as_view(), name= 'role edit')
]
