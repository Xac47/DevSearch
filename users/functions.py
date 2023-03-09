from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from users.models import Skill, Profile


def paginateProfiles(request, profiles, results):
    page = request.GET.get('page')
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, profiles

def searchProfiles(request):
    profiles = Profile.objects.all().order_by('-created')
    search = request.GET.get('q')
    if search:
        skill = Skill.objects.filter(name__icontains=search)
                                  # distinct() - убирает дубликаты
        profiles = Profile.objects.distinct().filter(
            Q(name__icontains=search) |
            Q(status_dev__icontains=search) |
            Q(skill__in=skill)
        ).order_by('-id')

    return profiles, search