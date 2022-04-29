from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from pages.models import *

def register(request):

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
             # Create a new user object but avoid saving it yet
             new_user = user_form.save(commit=False)
             # Set the chosen password
             new_user.set_password(user_form.cleaned_data['password'])
             # Save the User object
             new_user.save()

             # user profile
             Profile.objects.create(user=new_user)
             return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, 'account/register.html', {'user_form': user_form})


@login_required(login_url='login')
def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        usersong = Song.objects.filter(user=user)
        print("user :"+str(usersong))
        context={
            'songs':usersong
        }

    return render(request,'account/dashboard.html', context=context)

@login_required
def edit(request):

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def favourite_list(request):
    new = Song.newmanager.filter(favourites=request.user)
    return render(request, 'account/favourites.html', {'new': new})

@login_required
def favourite_add(request, id):
    song = get_object_or_404(Song, id=id)
    if song.favourites.filter(id=request.user.id).exists():
        song.favourites.remove(request.user)
    else:
        song.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
