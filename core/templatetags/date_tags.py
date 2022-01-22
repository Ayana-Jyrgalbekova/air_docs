import datetime

from django import template
from django.contrib import messages

register = template.Library()


@register.tag(name='today')
def dates(value):
    if value == datetime.date.today():
        messages.error(value, '"Дата исполнения" настала')
        return value
    else:
        pass
