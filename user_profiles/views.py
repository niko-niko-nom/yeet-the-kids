from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm, NewUserForm, UploadProfilePicture
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
        form = UserForm(request.POST)
        if not form.is_valid():
            return render(request, 'edit_profile.html', {'form': form})
        
        for i in form.changed_data:
            user[i] = form.cleaned_data[i]
        
        if form.is_valid():
            user.save()
            messages.success(request, "Dit profiel is succesvol bijgewerkt!")
            return redirect("profile", current_name=user.username)

    form = UserForm(initial={
        'pfp': user.pfp,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
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

    return render(request, 'edit_profile.html', {'form': form, 'profile': user})

@login_required
def user_profile_list(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if not form.is_valid():
            return render(request, 'list.html', {'form': form})
        
        user = User()
        user.username = form.cleaned_data['username']
        
        user.save()
        profiles = User.objects.all()
        messages.success(request, "Dit profiel is succesvol aangemaakt!")
        return render(request, 'list.html', {'profiles': profiles, 'form': form})

    profiles = User.objects.all()
    return render(request, 'list.html', {'profiles': profiles, 'form': form})

@login_required
def dashboard(request):
    profiles = User.objects.all()    
    return render(request, 'dashboard.html', {'profiles': profiles})


def upload_profile_picture(request, current_name):
    form = UploadProfilePicture()

    user = None
    try:
        user = User.objects.get(username__iexact=current_name)
    except User.DoesNotExist:
        return render(request, '404.html')

    if not request.user.has_perm("user.update") and request.user.id != user.id:
        return render(request, '404.html')

    if request.method == 'POST':
        form = UploadProfilePicture(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'profile_pic.html', {'form': form, 'profile': user})
        user.pfp = form.cleaned_data['pfp']
        user.save()
        return redirect("profile", current_name=current_name)

    return render(request, 'profile_pic.html', {'form': form, 'profile': user})

