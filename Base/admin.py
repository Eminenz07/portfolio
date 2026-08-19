from django.contrib import admin
from Base.models import Contact, Project, Skill, SiteProfile

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "created_at", "is_read"]
    list_filter = ["is_read", "created_at"]
    search_fields = ["name", "email", "message"]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "meta_category", "order", "created_at"]
    list_editable = ["order"]
    search_fields = ["title", "description", "tech_tags"]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "cluster", "level", "order"]
    list_filter = ["cluster", "level"]
    list_editable = ["order"]
    search_fields = ["name"]

@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    list_display = ["title_role", "email", "phone", "availability"]
