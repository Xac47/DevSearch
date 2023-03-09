import uuid

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True, blank=True)
    name = models.CharField('Имя/Фамилия', max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=555, null=True, blank=True)
    status_dev = models.CharField('Статус разработчика', max_length=255, null=True, blank=True)
    bio = models.TextField('Биография', null=True, blank=True)
    location = models.CharField('Место нахождения', max_length=255, null=True, blank=True)
    profile_image = models.ImageField('Фото профиля', default='user-default.png', upload_to='user_images/%Y/%m/%d/%h/%S/',
                                      null=True, blank=True)
    social_github = models.CharField('Ссылка на github', max_length=255, null=True, blank=True)
    social_twitter = models.CharField('Ссылка на twitter', max_length=255, null=True, blank=True)
    social_vk = models.CharField('Ссылка на vk', max_length=255, null=True, blank=True)
    social_telegram = models.CharField('Ссылка на telegram', max_length=255, null=True, blank=True)
    social_youtube = models.CharField('Ссылка на youtube', max_length=255, null=True, blank=True)
    social_website = models.CharField('Ссылка на вебсайт', max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    subscriptions = models.ManyToManyField('Profile', blank=True, verbose_name='Подписки', related_name='subscribers')


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.username


class Skill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField('Навык', max_length=100)
    desc = models.TextField('Навыки без описание будут добавляться как другие навыки', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    auther = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.name


# class Message(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#     body = models.TextField('Сообщение')
#     sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name='sender_messages')
#     recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name='recipient_messages')
#     created = models.DateTimeField('Создан', auto_now_add=True)