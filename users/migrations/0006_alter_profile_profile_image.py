# Generated by Django 4.1.5 on 2023-01-28 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='user-default.png', null=True, upload_to='user_images/%Y/%m/%d/%h/%S/', verbose_name='Фото профиля'),
        ),
    ]
