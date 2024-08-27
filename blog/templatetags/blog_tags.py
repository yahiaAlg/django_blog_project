import markdown
from django import template
from django.utils.safestring import mark_safe
from blog.models import Post

register = template.Library()


@register.filter(name="markdown")
def markdow_filter(value):
    return mark_safe(markdown.markdown(value))


@register.simple_tag
def total_published_posts():
    return Post.published.count()


@register.inclusion_tag("blog/partials/_latest_posts.html")
def show_latest_posts(count=2):
    latest_posts = Post.published.order_by("-publish")[:count]
    return {"latest_posts": latest_posts}
