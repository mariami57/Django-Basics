from django import template

from Regular_Exam___22_June_2025.utils import get_organizer

register = template.Library()

@register.simple_tag
def get_user():
    return get_organizer()