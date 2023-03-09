from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from projects.forms import CreateProjectForm, CreateReviewForm
from projects.functions import searchProjects, paginateProjects
from projects.models import Project, Tag, Review


def projects(request):
    projects, search = searchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 6)

    context = {
        'projects': projects,
        'search': search or '',
        'search_title': 'Поиск по названию проекта',
        'search_placeholder': 'Поиск по названию проекта',
        'custom_range': custom_range,
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    object = Project.objects.get(id=pk)
    form = CreateReviewForm()

    """ Просмотры """
    if request.user.is_authenticated:
        profile = request.user.profile
        user = object.views.filter(id=profile.id)
        if not user.exists():
            object.views.add(profile)

    """ Комментарии """
    if request.method == 'POST' and object.on_off_review:
        form = CreateReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent'):
                form.parent_id = request.POST.get('parent')
            form.project = object
            form.auther = request.user.profile
            form.save()
            return redirect('project', pk)

    context = {
        'object': object,
        'form': form
    }

    return render(request, 'projects/single-project.html', context)


@login_required
def create_project(request):
    a = 1
    profile = request.user.profile
    form = CreateProjectForm()

    if request.method == 'POST':
        form = CreateProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.auther = profile
            form.save()

            form.tags.add(*request.POST.getlist('tags'))

            return redirect('project', form.id)

    context = {
        'form': form,
        'a': a
    }

    return render(request, 'projects/create-project.html', context)


@login_required
def update_project(request, pk):
    try:
        profile = request.user.profile
        post = profile.project_set.get(id=pk)
        form = CreateProjectForm(instance=post)

        if request.method == 'POST':
            form = CreateProjectForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form = form.save(commit=False)
                form.auther = profile
                form.save()

                form.tags.add(*request.POST.getlist('tags'))

                return redirect('project', pk)
    except ObjectDoesNotExist:
        return redirect('project', pk)

    context = {
        'form': form
    }

    return render(request, 'projects/create-project.html', context)


@login_required
def delete_project(request, pk):
    try:
        profile = request.user.profile
        post = profile.project_set.get(id=pk)

        if request.method == 'POST':
            post.delete()
            return redirect('account')

    except ObjectDoesNotExist:
        return redirect('project', pk)

    context = {
        'object': post
    }

    return render(request, 'projects/delete-project.html', context)


@login_required
def delete_review(request, pk):
    # profile = request.user.profile
    # review = profile.my_review.get(id=pk)

    review = Review.objects.get(id=pk)
    profile = request.user.profile
    if profile == review.auther or profile == review.project.auther:
        review.delete()
    else:
        return redirect('project', review.project.pk)

    return HttpResponseRedirect(
        request.META['HTTP_REFERER'])  # возвращает пользователя на ту страницу в котором он совершил данную операция


@login_required
def check_likes(request, pk):
    object = Project.objects.get(id=pk)
    profile = request.user.profile
    project = object.likes.filter(id=profile.id)
    if project.exists():
        object.likes.remove(profile)
    else:
        object.likes.add(profile)
        object.dis_likes.remove(profile)

    return HttpResponseRedirect(
        request.META['HTTP_REFERER'])  # возвращает пользователя на ту страницу в котором он совершил данную операция


@login_required
def check_dislikes(request, pk):
    object = Project.objects.get(id=pk)
    profile = request.user.profile
    project = object.dis_likes.filter(id=profile.id)
    if project.exists():
        object.dis_likes.remove(profile)
    else:
        object.dis_likes.add(profile)
        object.likes.remove(profile)

    return HttpResponseRedirect(
        request.META['HTTP_REFERER'])  # возвращает пользователя на ту страницу в котором он совершил данную операция
