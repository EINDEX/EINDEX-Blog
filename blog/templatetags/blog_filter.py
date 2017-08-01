import datetime
from django import template

register = template.Library()


@register.filter
def daysince(value, arg):
    today = datetime.datetime.today()
    diff = today - value
    if arg == 'int':
        return diff
    if diff.days > 1:
        return '%s 天前' % diff.days
    elif diff.days == 1:
        return '昨天'
    elif diff.days == 0:
        return '今天'
    else:
        # Date is in the future; return formatted date.
        return value.strftime("%B %d, %Y")
