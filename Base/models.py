from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=1000)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.email}"

class Project(models.Model):
    title = models.CharField(max_length=150)
    meta_category = models.CharField(max_length=100, default="web app · api", help_text="e.g. web app · api")
    description = models.TextField()
    tech_tags = models.CharField(max_length=250, help_text="Comma-separated tags, e.g. Django, HTML, HTMX, CSS")
    browser_url = models.CharField(max_length=150, help_text="Display URL in browser bar, e.g. django-blog-api-292e.onrender.com")
    image = models.ImageField(upload_to="images/", blank=True, null=True, help_text="Upload preview image")
    image_static_path = models.CharField(max_length=200, blank=True, null=True, help_text="Or static image path, e.g. images/blog.png")
    live_demo_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title

    @property
    def tags_list(self):
        if self.tech_tags:
            return [tag.strip() for tag in self.tech_tags.split(",") if tag.strip()]
        return []

class Skill(models.Model):
    CLUSTER_CHOICES = [
        ("Backend", "Backend"),
        ("Frontend", "Frontend"),
        ("Data & AI", "Data & AI"),
        ("Infra & DevOps", "Infra & DevOps"),
    ]
    LEVEL_CHOICES = [
        ("Advanced", "Advanced"),
        ("Intermediate", "Intermediate"),
        ("Beginner", "Beginner"),
    ]

    cluster = models.CharField(max_length=50, choices=CLUSTER_CHOICES, default="Backend")
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES, default="Intermediate")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return f"{self.name} ({self.cluster} - {self.level})"

class SiteProfile(models.Model):
    title_role = models.CharField(max_length=150, default="Full Stack Developer")
    hero_role_text = models.CharField(max_length=250, default="builds reliable web apps with Django, Python & HTMX")
    status_message = models.CharField(max_length=250, default="open to new projects | let's build something worth shipping.")
    availability = models.CharField(max_length=150, default="Available for new projects")
    location = models.CharField(max_length=150, default="Nigeria · UTC+1 · remote friendly")
    bio_p1 = models.TextField(default="I'm a full-stack developer who loves solving real problems with code. Using tools like Django, Python and JavaScript, I build efficient, modern web applications with clean design and solid performance.")
    bio_p2 = models.TextField(default="I focus on delivering real-world solutions that are reliable, easy to use and built to scale, from API backends to Dockerised deployments.")
    email = models.EmailField(default="emmyadeoluwa@gmail.com")
    phone = models.CharField(max_length=50, default="+234 907 360 1282")
    twitter_url = models.URLField(default="https://x.com/Emidveloper")
    github_url = models.URLField(default="https://github.com/Eminenz07")
    profile_image = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return "Site Profile Settings"
