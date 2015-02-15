# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm
from profiles.forms import ProfileForm


def signup(request):
    if request.method == 'GET':
        user_form = UserCreationForm()
        profile_form = ProfileForm()
    elif request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            _user = user_form.save()
            _user.set_password(user_form.cleaned_data['password1'])
            _user.save()

            _profile = profile_form.save(commit=False)
            _profile.user = _user
            _profile.save()

            return HttpResponseRedirect('/photos/create/')

    return render(request, 'signup.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        })