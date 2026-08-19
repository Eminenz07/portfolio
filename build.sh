#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Auto-configure admin superuser and default profile on deploy
python manage.py shell -c "from django.contrib.auth.models import User; u, created = User.objects.get_or_create(username='eminence', defaults={'email': 'emmyadeoluwa@gmail.com', 'is_superuser': True, 'is_staff': True}); u.set_password('admin12345'); u.is_superuser = True; u.is_staff = True; u.save(); from Base.models import SiteProfile; SiteProfile.objects.get_or_create(pk=1)"
