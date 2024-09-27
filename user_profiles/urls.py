from django.urls import path
from .views import profile_view, edit_profile, user_profile_list, upload_profile_picture

urlpatterns = [
    path('<str:current_name>', profile_view, name='profile'),
    path('<str:current_name>/edit', edit_profile, name='edit_profile'),
    path('<str:current_name>/pic', upload_profile_picture, name='upload_profile_picture'),
    path('', user_profile_list, name='user_profile_list'),
]
