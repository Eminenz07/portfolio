from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Contact, Project, Skill, SiteProfile
from .forms import LoginForm, ProjectForm, SkillForm, SiteProfileForm

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    site_profile = SiteProfile.objects.first()
    if not site_profile:
        site_profile = SiteProfile.objects.create()

    # Group skills by cluster
    skills_by_cluster = {}
    for skill in skills:
        cluster = skill.cluster
        if cluster not in skills_by_cluster:
            skills_by_cluster[cluster] = []
        skills_by_cluster[cluster].append(skill)

    context = {
        "projects": projects,
        "skills": skills,
        "skills_by_cluster": skills_by_cluster,
        "site_profile": site_profile,
    }
    return render(request, "home.html", context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        message = (request.POST.get("message") or request.POST.get("content") or "").strip()

        if len(name) < 2 or len(name) > 40:
            messages.error(request, "Length of name should be between 2 and 40 characters.")
            return redirect('/#contact')

        if len(email) < 3 or len(email) > 50:
            messages.error(request, "Please provide a valid email address.")
            return redirect('/#contact')

        if not message:
            messages.error(request, "Please enter your message before submitting.")
            return redirect('/#contact')

        if phone and (len(phone) < 7 or len(phone) > 15):
            messages.error(request, "Invalid phone number, please try again.")
            return redirect('/#contact')

        ins = Contact(name=name, email=email, message=message, phone=phone)
        ins.save()

        messages.success(request, "Thank you for reaching out! Your message has been sent successfully.")
        return redirect('/#contact')

    return redirect('/#contact')

# ── DASHBOARD VIEWS ──────────────────────────────────────────

def admin_login(request):
    if request.user.is_authenticated:
        return redirect("dashboard_index")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect("dashboard_index")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, "dashboard/login.html", {"form": form})

def admin_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect("admin_login")

@login_required(login_url="admin_login")
def dashboard_index(request):
    total_projects = Project.objects.count()
    total_skills = Skill.objects.count()
    total_messages = Contact.objects.count()
    unread_messages = Contact.objects.filter(is_read=False).count()
    recent_messages = Contact.objects.all()[:5]

    context = {
        "total_projects": total_projects,
        "total_skills": total_skills,
        "total_messages": total_messages,
        "unread_messages": unread_messages,
        "recent_messages": recent_messages,
        "active_tab": "index",
    }
    return render(request, "dashboard/index.html", context)

@login_required(login_url="admin_login")
def dashboard_projects(request):
    projects = Project.objects.all()
    return render(request, "dashboard/projects_list.html", {"projects": projects, "active_tab": "projects"})

@login_required(login_url="admin_login")
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Project created successfully!")
            return redirect("dashboard_projects")
    else:
        form = ProjectForm()
    return render(request, "dashboard/project_form.html", {"form": form, "title": "Add New Project", "active_tab": "projects"})

@login_required(login_url="admin_login")
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project updated successfully!")
            return redirect("dashboard_projects")
    else:
        form = ProjectForm(instance=project)
    return render(request, "dashboard/project_form.html", {"form": form, "title": f"Edit Project: {project.title}", "active_tab": "projects"})

@login_required(login_url="admin_login")
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project deleted successfully!")
        return redirect("dashboard_projects")
    return render(request, "dashboard/confirm_delete.html", {"object": project, "type": "Project", "active_tab": "projects"})

@login_required(login_url="admin_login")
def dashboard_skills(request):
    skills = Skill.objects.all()
    return render(request, "dashboard/skills_list.html", {"skills": skills, "active_tab": "skills"})

@login_required(login_url="admin_login")
def skill_create(request):
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill added successfully!")
            return redirect("dashboard_skills")
    else:
        form = SkillForm()
    return render(request, "dashboard/skill_form.html", {"form": form, "title": "Add New Skill", "active_tab": "skills"})

@login_required(login_url="admin_login")
def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill updated successfully!")
            return redirect("dashboard_skills")
    else:
        form = SkillForm(instance=skill)
    return render(request, "dashboard/skill_form.html", {"form": form, "title": f"Edit Skill: {skill.name}", "active_tab": "skills"})

@login_required(login_url="admin_login")
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill deleted successfully!")
        return redirect("dashboard_skills")
    return render(request, "dashboard/confirm_delete.html", {"object": skill, "type": "Skill", "active_tab": "skills"})

@login_required(login_url="admin_login")
def dashboard_profile(request):
    profile = SiteProfile.objects.first()
    if not profile:
        profile = SiteProfile.objects.create()

    if request.method == "POST":
        form = SiteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Site profile updated successfully!")
            return redirect("dashboard_profile")
    else:
        form = SiteProfileForm(instance=profile)

    return render(request, "dashboard/profile_form.html", {"form": form, "active_tab": "profile"})

@login_required(login_url="admin_login")
def dashboard_messages(request):
    contact_messages = Contact.objects.all()
    return render(request, "dashboard/messages_list.html", {"contact_messages": contact_messages, "active_tab": "messages"})

@login_required(login_url="admin_login")
def message_toggle_read(request, pk):
    msg = get_object_or_404(Contact, pk=pk)
    msg.is_read = not msg.is_read
    msg.save()
    messages.info(request, "Message status updated.")
    return redirect("dashboard_messages")

@login_required(login_url="admin_login")
def message_delete(request, pk):
    msg = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        msg.delete()
        messages.success(request, "Message deleted successfully.")
        return redirect("dashboard_messages")
    return render(request, "dashboard/confirm_delete.html", {"object": f"Message from {msg.name}", "type": "Message", "active_tab": "messages"})
