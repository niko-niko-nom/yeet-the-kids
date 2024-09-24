from django.urls import path
from . import views
from . import models

urlpatterns = [
    path("", views.RoleListView.as_view(), name='roles'),
    path("<int:id>/", views.RolesView.as_view(), name='role'),

]
