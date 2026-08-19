from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),

    # Dashboard Auth
    path("dashboard/login/", views.admin_login, name="admin_login"),
    path("dashboard/logout/", views.admin_logout, name="admin_logout"),

    # Dashboard Views
    path("dashboard/", views.dashboard_index, name="dashboard_index"),
    path("dashboard/projects/", views.dashboard_projects, name="dashboard_projects"),
    path("dashboard/projects/new/", views.project_create, name="project_create"),
    path("dashboard/projects/<int:pk>/edit/", views.project_edit, name="project_edit"),
    path("dashboard/projects/<int:pk>/delete/", views.project_delete, name="project_delete"),

    path("dashboard/skills/", views.dashboard_skills, name="dashboard_skills"),
    path("dashboard/skills/new/", views.skill_create, name="skill_create"),
    path("dashboard/skills/<int:pk>/edit/", views.skill_edit, name="skill_edit"),
    path("dashboard/skills/<int:pk>/delete/", views.skill_delete, name="skill_delete"),

    path("dashboard/profile/", views.dashboard_profile, name="dashboard_profile"),

    path("dashboard/messages/", views.dashboard_messages, name="dashboard_messages"),
    path("dashboard/messages/<int:pk>/toggle-read/", views.message_toggle_read, name="message_toggle_read"),
    path("dashboard/messages/<int:pk>/delete/", views.message_delete, name="message_delete"),
]
