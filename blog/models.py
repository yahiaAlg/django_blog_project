from django.db import models
from django.urls import reverse
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class PublishedCommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Comment.Status.PUBLISHED)


# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="posts"
    )
    slug = models.SlugField(max_length=255, unique_for_date="publish")

    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"
        ARCHIVED = "archived", "Archived"

    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.DRAFT
    )

    published = PublishedManager()
    objects = models.Manager()

    class Meta:
        ordering = [
            "-publish",
        ]
        indexes = [models.Index(fields=["-publish"])]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            kwargs={
                "year": self.publish.year,
                "month": self.publish.month,
                "day": self.publish.day,
                "slug": self.slug,
            },
        )


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    email = models.EmailField(max_length=254)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)

    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"
        ARCHIVED = "archived", "Archived"

    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.PUBLISHED
    )
    likes_count = models.IntegerField(default=0)

    class Meta:
        ordering = ["-publish"]
        indexes = [models.Index(fields=["-publish"])]

    published = PublishedCommentManager()
    objects = models.Manager()

    def __str__(self):
        return self.content[:15]
