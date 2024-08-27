import django
from blog.models import Post

# Dictionary of titles and their corresponding tags
titles_and_tags = {
    "The Future of Web Development": ["Future", "Web Development", "Technology"],
    "A Beginner's Guide to Django": [
        "Django",
        "Beginner",
        "Guide",
        "Programming",
        "Technology",
    ],
    "Understanding REST APIs": ["REST APIs", "APIs", "Web Development", "Programming"],
}

# Adding tags to the posts
for title, tags in titles_and_tags.items():
    try:
        post = Post.objects.get(title=title)
        post.tags.add(*tags)
        print(f"Tags {tags} added to post '{title}'")
    except Post.DoesNotExist:
        print(f"Post with title '{title}' does not exist")
