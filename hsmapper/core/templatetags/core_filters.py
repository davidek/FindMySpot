from datetime import datetime
from django import template

register = template.Library()

@register.filter
def in_the_past(date):
    return date < datetime.now()

@register.filter
def get_item(list_, index):
    try:
        return list_[int(index)]
    except (ValueError, TypeError, IndexError):
        return u""

@register.filter
def filter_wd(queryset, weekday):
    return queryset.filter(weekday=weekday[0]).order_by("id")
