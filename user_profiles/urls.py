from django.urls import path
from .views import profile_view, edit_profile

urlpatterns = [
    path('<str:current_name>', profile_view, name='profile'),
    path('<str:current_name>/edit', edit_profile, name='edit_profile'),
]
