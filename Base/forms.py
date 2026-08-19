from django import forms
from .models import Project, Skill, SiteProfile

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Username", "class": "field-input", "required": True})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "field-input", "required": True})
    )

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "meta_category",
            "description",
            "tech_tags",
            "browser_url",
            "image",
            "image_static_path",
            "live_demo_url",
            "github_url",
            "order",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "e.g. Django Blog API", "class": "field-input"}),
            "meta_category": forms.TextInput(attrs={"placeholder": "e.g. web app · api", "class": "field-input"}),
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Project description...", "class": "field-input"}),
            "tech_tags": forms.TextInput(attrs={"placeholder": "e.g. Django, HTML, HTMX, CSS", "class": "field-input"}),
            "browser_url": forms.TextInput(attrs={"placeholder": "e.g. django-blog-api-292e.onrender.com", "class": "field-input"}),
            "image_static_path": forms.TextInput(attrs={"placeholder": "e.g. images/blog.png", "class": "field-input"}),
            "live_demo_url": forms.URLInput(attrs={"placeholder": "https://demo-url.com", "class": "field-input"}),
            "github_url": forms.URLInput(attrs={"placeholder": "https://github.com/...", "class": "field-input"}),
            "order": forms.NumberInput(attrs={"class": "field-input"}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ["cluster", "name", "level", "order"]
        widgets = {
            "cluster": forms.Select(attrs={"class": "field-input"}),
            "name": forms.TextInput(attrs={"placeholder": "e.g. Python", "class": "field-input"}),
            "level": forms.Select(attrs={"class": "field-input"}),
            "order": forms.NumberInput(attrs={"class": "field-input"}),
        }

class SiteProfileForm(forms.ModelForm):
    class Meta:
        model = SiteProfile
        fields = [
            "title_role",
            "hero_role_text",
            "status_message",
            "availability",
            "location",
            "bio_p1",
            "bio_p2",
            "email",
            "phone",
            "twitter_url",
            "github_url",
        ]
        widgets = {
            "title_role": forms.TextInput(attrs={"class": "field-input"}),
            "hero_role_text": forms.TextInput(attrs={"class": "field-input"}),
            "status_message": forms.TextInput(attrs={"class": "field-input"}),
            "availability": forms.TextInput(attrs={"class": "field-input"}),
            "location": forms.TextInput(attrs={"class": "field-input"}),
            "bio_p1": forms.Textarea(attrs={"rows": 4, "class": "field-input"}),
            "bio_p2": forms.Textarea(attrs={"rows": 4, "class": "field-input"}),
            "email": forms.EmailInput(attrs={"class": "field-input"}),
            "phone": forms.TextInput(attrs={"class": "field-input"}),
            "twitter_url": forms.URLInput(attrs={"class": "field-input"}),
            "github_url": forms.URLInput(attrs={"class": "field-input"}),
        }
