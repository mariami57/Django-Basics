from django import template

from Retake_Exam___13_December_2024.utils import get_traveler

register = template.Library()

@register.simple_tag
def get_user():
    return get_traveler()