from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    # path("", views.post_list, name="post_list"),
    path("", views.PostListView.as_view(), name="post_list"),
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
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
]
