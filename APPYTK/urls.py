from django.urls import path

from . import views
from user_profiles.views import dashboard

urlpatterns = [
    path("", views.home, name="home"),
    path("hbo-ict/", views.hboict, name="hbo"),
    path("scrum/", views.scrum, name="scrum"),
    path("dashboard/", dashboard, name="dashboard")
]
  
