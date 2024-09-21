from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def profile_view(request, username):
    # Fetch the user by their username
    user = get_object_or_404(User, username=username)
    
    # Pass the user data to the template
    return render(request, 'profile.html', {'user': user})
