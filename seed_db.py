import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
django.setup()

from django.contrib.auth.models import User
from Base.models import Project, Skill, SiteProfile

def seed():
    # 1. Superuser
    u, created = User.objects.get_or_create(
        username="eminence",
        defaults={"email": "emmyadeoluwa@gmail.com", "is_superuser": True, "is_staff": True}
    )
    u.set_password("admin12345")
    u.is_superuser = True
    u.is_staff = True
    u.save()
    print("Admin superuser 'eminence' configured.")

    # 2. Site Profile
    profile, _ = SiteProfile.objects.get_or_create(pk=1)
    print("SiteProfile initialized.")

    # 3. Projects
    projects_data = [
        {
            "title": "SubHero",
            "meta_category": "fintech · vtu & smm platform",
            "description": "An all-in-one Nigerian fintech platform for instant VTU airtime, affordable data bundles, utility bills, and automated social media growth with dedicated virtual accounts and atomic zero-fee P2P wallet transfers.",
            "tech_tags": "Django, PostgreSQL, Redis, Celery, HTMX, Tailwind CSS",
            "browser_url": "subhero-smm.onrender.com",
            "image_static_path": "images/subhero.png",
            "live_demo_url": "https://subhero-smm.onrender.com/",
            "github_url": "https://gitlab.com/His_emi/subhero",
            "order": 1,
        },
        {
            "title": "The Truth Gate",
            "meta_category": "platform · live",
            "description": "An institutional-grade, faith-based platform offering sermons, WebSocket-powered live counselling and community interaction, built around emotional safety, privacy and secure donations.",
            "tech_tags": "Django, Channels, Redis, PostgreSQL, Paystack",
            "browser_url": "the-truth-gate.onrender.com",
            "image_static_path": "images/TruthGate.png",
            "live_demo_url": "https://the-truth-gate.onrender.com/",
            "github_url": "https://github.com/Eminenz07/the_truth_gate",
            "order": 2,
        },
        {
            "title": "Trade With Ariel",
            "meta_category": "marketing site · cms",
            "description": "A premium single-page marketing site for a trading brand with institutional-grade glassmorphism design and a bespoke Django CMS managing mentorships and marketplace offers.",
            "tech_tags": "Django, HTML5, CSS3, Vanilla JS",
            "browser_url": "tradewithariel.onrender.com",
            "image_static_path": "images/TWAriel.png",
            "live_demo_url": "https://tradewithariel.onrender.com/",
            "github_url": "https://github.com/Eminenz07/tradewithariel",
            "order": 3,
        },
        {
            "title": "SubDoc",
            "meta_category": "dev tool · privacy-first",
            "description": "A private, stateless PDF-to-Word conversion app with OCR fallback for scanned PDFs and a sleek drag-and-drop interface.",
            "tech_tags": "Flask, Python, Docker",
            "browser_url": "subdoc-582204185999.us-central1.run.app",
            "image_static_path": "images/SubDoc (1).png",
            "live_demo_url": "https://subdoc-582204185999.us-central1.run.app/",
            "github_url": "https://github.com/Eminenz07/subdoc",
            "order": 4,
        },
        {
            "title": "AU Voting System",
            "meta_category": "platform · election mgmt",
            "description": "A comprehensive election management system for candidate management, dynamic polling and secure vote counting with a responsive front-end interface.",
            "tech_tags": "Django, SQLite, Bootstrap",
            "browser_url": "au-voting-system-chi.vercel.app",
            "image_static_path": "images/AU Voting system.png",
            "live_demo_url": "https://au-voting-system-chi.vercel.app/",
            "github_url": "https://github.com/Eminenz07/voting-system2",
            "order": 5,
        },
        {
            "title": "Django Blog API",
            "meta_category": "web app · api",
            "description": "A robust, scalable blog API built with Django featuring user authentication, post creation, editing and deletion, with a flexible architecture designed for expansion.",
            "tech_tags": "Django, HTML, HTMX, CSS",
            "browser_url": "django-blog-api-292e.onrender.com",
            "image_static_path": "images/blog.png",
            "live_demo_url": "https://django-blog-api-292e.onrender.com",
            "github_url": "https://github.com/Eminenz07/django-blog-api",
            "order": 6,
        },
        {
            "title": "VA Portfolio",
            "meta_category": "website · personal brand",
            "description": "A sleek, professional portfolio tailored for a virtual assistant displaying services, skills and client testimonials elegantly.",
            "tech_tags": "HTML5, CSS3, JavaScript",
            "browser_url": "excellenceeniola.fly.dev",
            "image_static_path": "images/VA Assistant.png",
            "live_demo_url": "https://excellenceeniola.fly.dev/",
            "github_url": "https://github.com/Eminenz07/virtual-assistant-portfolio",
            "order": 7,
        },
    ]
    for p in projects_data:
        obj, created = Project.objects.update_or_create(
            title=p["title"],
            defaults=p
        )
    print(f"Synced {len(projects_data)} projects into database.")

    # 4. Skills
    if Skill.objects.count() == 0:
        skills_data = [
            ("Backend", "Python", "Advanced", 1),
            ("Backend", "Django", "Intermediate", 2),
            ("Backend", "Java", "Beginner", 3),
            ("Backend", "C/C++", "Beginner", 4),
            ("Frontend", "HTML", "Advanced", 1),
            ("Frontend", "CSS", "Intermediate", 2),
            ("Frontend", "HTMX", "Intermediate", 3),
            ("Frontend", "JavaScript", "Beginner", 4),
            ("Data & AI", "SQL", "Intermediate", 1),
            ("Data & AI", "SQLite", "Intermediate", 2),
            ("Data & AI", "AI/ML", "Beginner", 3),
            ("Infra & DevOps", "Docker", "Intermediate", 1),
            ("Infra & DevOps", "Git", "Intermediate", 2),
            ("Infra & DevOps", "VPS", "Intermediate", 3),
        ]
        for cluster, name, level, order in skills_data:
            Skill.objects.create(cluster=cluster, name=name, level=level, order=order)
        print(f"Seeded {len(skills_data)} skills into database.")

if __name__ == "__main__":
    seed()
