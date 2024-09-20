from django.urls import path

from . import views
from .views.loginView import LoginView

urlpatterns = [
    path("login", LoginView.as_view(), name='login')
]
