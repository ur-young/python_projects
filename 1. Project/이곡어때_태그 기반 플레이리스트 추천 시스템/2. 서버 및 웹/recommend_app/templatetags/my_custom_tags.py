from django import template

register = template.Library()

@register.filter
def toplus(value):
    return value.replace(' ',"+")