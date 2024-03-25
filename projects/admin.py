from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from projects.models import Project, Review, Tag


class ProjectAdminForm(forms.ModelForm):
    desc = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Project
        fields = '__all__'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'auther')
    list_display_links = ('id', 'title', 'auther')
    form = ProjectAdminForm
    save_on_top = True
    save_as = True


admin.site.register(Review)
admin.site.register(Tag)
