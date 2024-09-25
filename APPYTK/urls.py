from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hbo-ict/", views.hboict, name="hbo"),
]
  
