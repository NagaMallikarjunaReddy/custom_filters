from django import template

register=template.Library()


def swap(value):
    return value.swapcase()

register.filter('swap',swap)


@register.filter(name='count')
def count(value,arg):
    c=0
    for i in range(len(value)):
        if arg==value[i:i+len(arg)]:
            c+=1
    return c
@register.filter()
def remove(value,arg):
    return value.replace(arg,'')