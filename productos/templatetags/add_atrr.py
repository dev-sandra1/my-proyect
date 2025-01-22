from django import template
refister = template.Library()

@register.filter(name="add_attr")
def add_attr(field, css):
    attrs = {}
    clase, valor = css.split(':')
    attrs['clase'] = valor

    return field.as_widget(attrs=attrs)