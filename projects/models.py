from django.db import models

import uuid

from users.models import Profile


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField('Заголовок', max_length=200)
    desc = models.TextField('Описание', null=True, blank=True)
    image = models.ImageField('Фото', null=True, blank=True, default='default.jpg',
                              upload_to='project_images/%Y/%m/%d/%h/%S/')
    demo_link = models.CharField('Демонстрационная ссылка', max_length=2000, null=True, blank=True)
    source_link = models.CharField('Ссылка на источник', max_length=2000, null=True, blank=True)
    vote_total = models.IntegerField('Общее количество голосов', default=0, null=True, blank=True)
    vote_ratio = models.IntegerField('Соотношение голосов', default=0, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='Теги')
    created = models.DateTimeField('Опубликовано', auto_now_add=True)
    auther = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    on_off_review = models.BooleanField('Комментарии Вкл/Выкл', default=True)
    views = models.ManyToManyField(Profile, blank=True, related_name='views')
    likes = models.ManyToManyField(Profile, verbose_name='Лайки', related_name='my_likes', blank=True)
    dis_likes = models.ManyToManyField(Profile, verbose_name='Дизлайки', related_name='my_dislikes', blank=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title

    def get_review(self):
        return self.review_set.filter(parent__isnull=True)


class Review(models.Model):
    VOTE_TYPE = (
        ('за', 'Голосовать за'),
        ('против', 'Проголосовать против'),
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    body = models.TextField('Описание', null=True, blank=True)
    value = models.CharField('Значение', max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField('Дата', auto_now_add=True)
    auther = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='my_review')
    parent = models.ForeignKey('Review', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.body

    def get_answers(self):
        return self.review_set.filter(parent__isnull=False)


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField('Название', max_length=200)
    created = models.DateTimeField('Создан', auto_now_add=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name
