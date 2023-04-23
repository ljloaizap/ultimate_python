from django import template
register = template.Library()


@register.filter(name='add_attr')
def add_attr(field, css):
    attrs = {}
    class_name, value = css.split(':')
    attrs[class_name] = value
    return field.as_widget(attrs=attrs)
