from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from projects.models import Project, Tag


def paginateProjects(request, projects, results):

    page = request.GET.get('page')
    paginator = Paginator(projects, results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, projects

def searchProjects(request):
    projects = Project.objects.all().order_by('-created')
    search = request.GET.get('q')

    if search:
        tags = Tag.objects.filter(name__icontains=search)
                                  # distinct() - убирает дубликаты
        projects = Project.objects.distinct().filter(
            Q(title__icontains=search) |
            Q(tags__in=tags)
        ).order_by('-created')

    return projects, search
