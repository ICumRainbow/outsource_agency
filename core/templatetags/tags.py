import datetime

from django import template

register = template.Library()


@register.simple_tag
def format_date(value: datetime, time=False):
    if time:
        value = value.strftime("%B %d, %Y, %H:%M:%S")
    else:
        value = value.strftime("%B %d, %Y")
    return value


@register.simple_tag(takes_context=True)
def append_to_url(context, value, field_name):
    url = context['request'].GET.copy()
    url[field_name] = value

    return '?' + url.urlencode()
