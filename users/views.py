from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from users.forms import SignUpForm, UpdateProfileForm, CreateSkillForm
from users.functions import searchProfiles, paginateProfiles
from users.models import Profile, Skill


def profiles(request):
    profiles, search = searchProfiles(request)
    custom_range, profiles = paginateProfiles(request, profiles, 6)

    context = {
        'profiles': profiles,
        'search': search or '',
        'search_title': 'Поиск по разработчикам',
        'search_placeholder': 'Поиск по разработчикам',
        'custom_range': custom_range,
    }

    return render(request, 'users/profiles.html', context)


def profile(request, pk):
    object = Profile.objects.get(id=pk)

    skills = object.skill_set.exclude(desc__exact='')  # навыки у которых описание не пустое
    otherSkills = object.skill_set.filter(desc='')  # навыки с пустыми описаниями

    context = {
        'object': object,
        'skills': skills,
        'otherSkills': otherSkills,
    }

    return render(request, 'users/profile.html', context)


def _login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('account')
        messages.error(request, 'Не верный логин или пароль')

    return render(request, 'users/login.html')


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form = form.save()
            login(request, form)
            return redirect('account')

    context = {
        'form': form
    }
    return render(request, 'users/signup.html', context)


def exit(request):
    logout(request)
    return redirect('profiles')


@login_required
def account(request):
    profile = request.user.profile

    context = {
        'profile': profile
    }

    return render(request, 'users/account.html', context)


@login_required
def update_account(request):
    profile = request.user.profile
    form = UpdateProfileForm(instance=profile)

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('account')

    context = {
        'form': form
    }
    return render(request, 'users/update-account.html', context)


@login_required
def create_skill(request):
    a = 1
    profile = request.user.profile
    form = CreateSkillForm()
    if request.method == 'POST':
        form = CreateSkillForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.auther = profile
            form.save()

            return redirect('account')

    context = {
        'form': form,
        'a': a
    }

    return render(request, 'users/create-skill.html', context)


@login_required
def update_skill(request, pk):
    try:
        profile = request.user.profile
        object = profile.skill_set.get(id=pk)
        form = CreateSkillForm(instance=object)
        if request.method == 'POST':
            form = CreateSkillForm(request.POST, instance=object)
            if form.is_valid():
                form = form.save(commit=False)
                form.auther = profile
                form.save()
                return redirect('account')
    except ObjectDoesNotExist:
        return redirect('account')

    context = {
        'form': form
    }

    return render(request, 'users/create-skill.html', context)


@login_required
def delete_skill(request, pk):
    try:
        profile = request.user.profile
        object = profile.skill_set.get(id=pk)
        if request.method == 'POST':
            object.delete()
            return redirect('account')

    except ObjectDoesNotExist:
        return redirect('account')

    context = {
        'object': object
    }

    return render(request, 'users/delete-skill.html', context)


@login_required
def subscription_check(request, pk):
    profile = request.user.profile
    object = profile.subscriptions.filter(id=pk)

    if object.exists():
        profile.subscriptions.remove(pk)
    else:
        profile.subscriptions.add(pk)

    return HttpResponseRedirect(
        request.META['HTTP_REFERER'])  # возвращает пользователя на ту страницу в котором он совершил данную операция

