from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj: Post):
        return obj.updated_at

    def location(self, obj: Post):
        return obj.get_absolute_url()
