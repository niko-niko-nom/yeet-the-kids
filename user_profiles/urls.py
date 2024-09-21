from django.urls import path
from .views import profile_view

urlpatterns = [
    path('profile/{{ current_name }}', profile_view, name='profile'),
]
