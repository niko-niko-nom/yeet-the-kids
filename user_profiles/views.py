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

@login_required
def edit_profile(request, current_name):

    user = None
    try:
        user = User.objects.get(username__iexact=current_name)
    except User.DoesNotExist:
        return render(request, '404.html')

    if not request.user.has_perm("user.update") and request.user.id != user.id:
        return render(request, '404.html')

    form = None

    if request.method == 'POST':
        form = UserData(request.POST)
        if not form.is_valid():
            return render(request, 'edit_profile.html', {'form': form})
        
        for i in form.changed_data:
            user[i] = form.cleaned_data[i]

        user.save()
        
        return redirect("profile", current_name=user.username)

    form = UserData(initial={
        'pfp': user.pfp,
        'username': user.username,
        'email': user.email,
        'age': user.birthday,
        'city': user.city,
        'gender': user.gender,
        'pronouns': user.pronouns,
        'number': user.number,
        'bio': user.bio,
        'trivia1': user.trivia1,
        'trivia2': user.trivia2,
        'trivia3': user.trivia3,
        'trivia4': user.trivia4,
        'trivia5': user.trivia5,
    })
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def user_profile_list(request):
    profiles = User.objects.all()
    return render(request, 'profiles/list.html', {'profiles': profiles})