from django import template
register = template.Library()

@register.filter
def kong_upper(val):

    return val.upper()

# 自定义标签
from django.utils.html import format_html
@register.simple_tag
def jia(a,b):
    ret = int(a)+int(b)
    return ret

# 自定义标签

