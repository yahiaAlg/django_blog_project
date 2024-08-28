from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap
from .feed import BlogFeed

sitemaps = {"posts": PostSitemap}


app_name = "blog"
urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("tag/<slug:tag_slug>/", views.post_list, name="post_list_by_tag"),
    # path("", views.PostListView.as_view(), name="post_list"),
    path("like_comment/<int:comment_id>/", views.like_comment, name="like_comment"),
    path(
        "dislike_comment/<int:comment_id>/",
        views.dislike_comment,
        name="dislike_comment",
    ),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:slug>/",
        views.post_detail,
        name="post_detail",
    ),
    path("share_post/<int:pk>/", views.share_post, name="share_post"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path(
        "feed/",
        BlogFeed(),
        name="post_feed",
    ),
    path("search/", views.post_list, name="post_search")
]
