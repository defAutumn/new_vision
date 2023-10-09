from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import RegistrationForm, EditProfileForm


# Create your views here.


@login_required
def home(request):
    return render(request, template_name='account/home.html')


@login_required
def profile(request):
    return render(request, template_name='account/profile.html')


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, template_name='account/register_done.html')
    else:
        user_form = RegistrationForm()
    return render(request, template_name='account/register.html', context={'form': user_form})


def edit(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=user)
        return render(request=request, template_name='account/edit_profile.html', context={'form': form})
