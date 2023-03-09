from django import forms

from projects.models import Project, Tag, Review


class CreateProjectForm(forms.ModelForm):
    title = forms.CharField(
        label='Заголовок',
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Заголовок'})
    )

    desc = forms.CharField(
        label='Описание',
        widget=forms.Textarea(attrs={'class': 'input', 'placeholder': 'Описание', 'rows': 14, 'cols': 50})
    )

    image = forms.FileField(
        required=False,
        label='Фото',
    )

    demo_link = forms.CharField(
        label='Демонстрационная ссылка',
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Демонстрационная ссылка'})
    )

    source_link = forms.CharField(
        label='Ссылка на источник',
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Ссылка на источник'})
    )

    tags = forms.ModelMultipleChoiceField(
        Tag.objects.all(),
        label='Теги',
    )

    class Meta:
        model = Project
        fields = ('title', 'desc', 'image', 'on_off_review', 'demo_link', 'source_link', 'tags')


    # def __init__(self, *args, **kwargs):
    #     # super(CreateProjectForm, self).__init__(*args, **kwargs)
    #     #
    #     # self.fields['title'].widget.attrs.update({'class': 'input'})

class CreateReviewForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        required=False,
        widget=forms.Textarea(attrs={'class': 'input', 'rows': 2, 'cols': 50, 'placeholder': 'Комментарии', 'id': 'contactcomment'})
    )

    class Meta:
        model = Review
        fields = ('value', 'body')