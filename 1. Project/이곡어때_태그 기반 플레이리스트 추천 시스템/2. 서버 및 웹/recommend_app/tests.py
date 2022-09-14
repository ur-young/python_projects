import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recommend_app.settings")

import django
django.setup()

from models import Post