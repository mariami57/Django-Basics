"""
WSGI config for Retake_Exam___17_April_2024 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Retake_Exam___17_April_2024.settings')

application = get_wsgi_application()
