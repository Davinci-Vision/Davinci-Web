from django import template
from ..models import Whitepaper
from django.db.models import Q

register = template.Library()

@register.inclusion_tag('layout/whitepaper.html', takes_context=True)
def download_whitepaper(context):

    data = {}
    q = Q(is_open=True)
    wp = Whitepaper.objects.filter(q).order_by('created_at')
    try:
        data["download"] = wp
    except Exception as e:
        data["download"] = "#"

    return data
