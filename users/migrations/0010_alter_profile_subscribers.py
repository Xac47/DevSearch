# Generated by Django 4.1.5 on 2023-02-05 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_profile_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='subscribers',
            field=models.ManyToManyField(blank=True, to='users.profile', verbose_name='Подписчики'),
        ),
    ]
