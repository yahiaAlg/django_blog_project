from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from markdown import markdown
from .models import Post


class BlogFeed(Feed):
    title = "Blog Feed"
    link = reverse_lazy("blog:post_list")
    description = "New Posts for my Blog"

    def items(self):
        return Post.objects.all()

    def item_title(self, item: Post):
        return item.title

    def item_description(self, item: Post):
        return truncatewords_html(markdown(item.content), 30)

    def item_link(self, item: Post):
        return item.get_absolute_url()

    def item_pubdate(self, item: Post):
        return item.publish

    def item_author_name(self, item: Post):
        return item.author.username

    def item_categories(self, item: Post):
        return item.tags.all()
