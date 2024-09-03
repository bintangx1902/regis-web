from django import template
from django.utils import timezone

register = template.Library()


@register.filter
def is_active(phase):
    now = timezone.now()
    return phase.open_on <= now <= phase.closed_on
