import markdown
from django import template

register = template.Library()


@register.simple_tag(name="markdown")
def markdown_format(html):
    return markdown.markdown(html)
