from django import template
register = template.Library()


@register.filter(name='chuyi')
def chuyi(value, arg):
    a = value/arg
    return '%.2f' % a

@register.filter(name='roundtwo')
def roundtwo(value):
    return '%.2f' % value