from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserData
from .models import User

@login_required
def profile_view(request, current_name):
    user = None
    try:
        user = User.objects.get(username__iexact=current_name)
    except User.DoesNotExist:
        return render(request, '404.html')

    return render(request, 'profile.html', {'user': user})

def edit_profile(request, current_name):
    form = UserData()
    return render(request, 'edit_profile.html', {'form': form})

def user_profile_list(request):
    profiles = User.objects.all()
    return render(request, 'profiles/list.html', {'profiles': profiles})