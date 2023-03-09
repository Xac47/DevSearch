from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from users.models import Profile, Skill


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'formInput#text', 'class': 'input'})
    )
    username = forms.CharField(
        error_messages={'unique': 'Пользователь с таким логином уже существует.'},
        widget=forms.TextInput(attrs={'id': 'formInput#text', 'class': 'input'})
    )
    email = forms.EmailField(
        error_messages={'unique': 'Пользователь с таким email уже существует.'},
        widget=forms.EmailInput(attrs={'id': 'formInput#email', 'class': 'input'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'formInput#password', 'class': 'input'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'formInput#confirm-password', 'class': 'input'})
    )

    class Meta:
        model = User
        fields = ('first_name', 'username',  'email', 'password1', 'password2')


class UpdateProfileForm(forms.ModelForm):
    name = forms.CharField(
        label='Имя/Фамилия',
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    username = forms.CharField(
        label='Логин',
        error_messages={'unique': 'Пользователь с таким логином уже существует.'},
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    email = forms.EmailField(
        label='Email',
        error_messages={'unique': 'Пользователь с таким email уже существует.'},
        widget=forms.EmailInput(attrs={'class': 'input'})
    )
    status_dev = forms.CharField(
        label='Статус разработчика',
        required=False,
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    bio = forms.CharField(
        label='ОБО МНЕ',
        required=False,
        widget=forms.Textarea(attrs={'class': 'input', 'rows': 10, 'cols': 50})
    )
    location = forms.CharField(
        label='Место нахождение',
        required=False,
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    profile_image = forms.FileField(
        label='Фото профиля',
        required=False,
    )
    social_github = forms.CharField(
        label='Ссылка на github',
        required=False,
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    social_twitter = forms.CharField(
        label='Ссылка на twitter',
        required=False,
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    social_vk = forms.CharField(
        label='Ссылка на vk',
        required=False,
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    social_telegram = forms.CharField(
        label='Ссылка на telegram',
        required=False,
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    social_youtube = forms.CharField(
        label='Ссылка на youtube',
        required=False,
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    social_website = forms.CharField(
        label='Ссылка на ваш website',
        required=False,
        widget=forms.TextInput(attrs={'class': 'input'})
    )

    class Meta:
        model = Profile
        fields = ('name', 'username', 'email', 'status_dev', 'bio',
                  'location', 'profile_image', 'social_github',
                  'social_twitter', 'social_vk', 'social_telegram',
                  'social_youtube', 'social_website')

class CreateSkillForm(forms.ModelForm):
    name = forms.CharField(
        label='Навык',
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    desc = forms.CharField(
        label='Пару слов об опыте на данном навыке',
        required=False,
        widget=forms.Textarea(attrs={'class': 'input', 'rows': 10, 'cols': 50})
    )

    class Meta:
        model = Skill
        fields = ('name', 'desc')