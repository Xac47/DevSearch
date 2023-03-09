from django.contrib import admin

from users.models import Profile, Skill


class SkillAdmin(admin.TabularInline):
    model = Skill
    fields = ('name', 'desc')
    extra = 0


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (SkillAdmin,)


admin.site.register(Skill)
