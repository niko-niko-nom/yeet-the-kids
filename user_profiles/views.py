from django.shortcuts import render, redirect
from .forms import UserData
from .models import User

def profile_view(request, current_name):
    # Check if the user is authenticated
    # if not request.user.is_authenticated:
    #    return redirect('login')  # Redirect to login if not authenticated

    # Get the user's current data (replace this with your actual user data retrieval logic)
    # current_data = {
    #     'name': request.user.get_full_name(),
    #     'age': request.user.profile.age,
    #     'city': request.user.profile.city,
    #     'gender': request.user.profile.gender,
    #     'pronouns': request.user.profile.pronouns,
    #     'number': request.user.profile.number,
    #     'email': request.user.email,
    #     'roles': request.user.profile.roles,  # Assuming roles are stored as a list
    #     'bio': request.user.profile.bio,
    #     'trivia1': request.user.profile.trivia1,
    #     'trivia2': request.user.profile.trivia2,
    #     'trivia3': request.user.profile.trivia3,
    #     'trivia4': request.user.profile.trivia4,
    #     'trivia5': request.user.profile.trivia5,
    # }

    # if request.method == 'POST':
    #     form = UserData(request.POST, request.FILES, initial=current_data)
    #     if form.is_valid():
    #         # Save the data (you'll need to implement the logic to update the user's profile)
    #         user_profile = request.user.profile  # Assuming you have a Profile model linked to User
    #         user_profile.age = form.cleaned_data['age']
    #         user_profile.city = form.cleaned_data['city']
    #         user_profile.gender = form.cleaned_data['gender']
    #         user_profile.pronouns = form.cleaned_data['pronouns']
    #         user_profile.number = form.cleaned_data['number']
    #         user_profile.bio = form.cleaned_data['bio']
    #         user_profile.trivia1 = form.cleaned_data['trivia1']
    #         user_profile.trivia2 = form.cleaned_data['trivia2']
    #         user_profile.trivia3 = form.cleaned_data['trivia3']
    #         user_profile.trivia4 = form.cleaned_data['trivia4']
    #         user_profile.trivia5 = form.cleaned_data['trivia5']
    #         user_profile.save()
    # else:
    form = UserData()

    return render(request, 'profile.html', {'form': form})

def edit_profile(request, current_name):

    form = UserData()

    return render(request, 'edit_profile.html', {'form': form})

def user_profile_list(request):
    profiles = User.objects.all()
    return render(request, 'profiles/list.html', {'profiles': profiles})
