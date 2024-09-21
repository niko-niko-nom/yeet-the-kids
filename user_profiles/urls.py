from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:user_name>/', views.profile_view, name='profile'),
]
