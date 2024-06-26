# Generated by Django 4.1.2 on 2023-03-10 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя/Фамилия')),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=555, null=True)),
                ('status_dev', models.CharField(blank=True, max_length=255, null=True, verbose_name='Статус разработчика')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Биография')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Место нахождения')),
                ('profile_image', models.ImageField(blank=True, default='user-default.png', null=True, upload_to='user_images/%Y/%m/%d/%h/%S/', verbose_name='Фото профиля')),
                ('social_github', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на github')),
                ('social_twitter', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на twitter')),
                ('social_vk', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на vk')),
                ('social_telegram', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на telegram')),
                ('social_youtube', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на youtube')),
                ('social_website', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на вебсайт')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('subscriptions', models.ManyToManyField(blank=True, related_name='subscribers', to='users.profile', verbose_name='Подписки')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100, verbose_name='Навык')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Навыки без описание будут добавляться как другие навыки')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
            },
        ),
    ]
