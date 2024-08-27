# from django.http import Http404
from django.views.generic import ListView

from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404

# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *


# Create your views here
# def post_list(request):
#     posts = Post.published.all()
#     paginator = Paginator(posts, 6)
#     page = request.GET.get("page", 1)
#     try:
#         posts = paginator.get_page(page)
#         context = {"posts": posts}
#     except PageNotAnInteger:
#         posts = paginator.get_page(1)
#     except EmptyPage:
#         posts = paginator.get_page(paginator.num_pages - 1)
#     finally:
#         return render(request, "blog/posts/post_list.html", context)
class PostListView(ListView):
    queryset = Post.published.all()
    paginate_by = 6
    context_object_name = "posts"
    template_name = "blog/posts/post_list.html"


from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Comment


@require_POST
def like_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.likes_count += 1
    comment.save()
    return JsonResponse({"success": True, "likes_count": comment.likes_count})


@require_POST
def dislike_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return JsonResponse({"success": True})


from .forms import CommentForm


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(
        Post.published,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=slug,
    )

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(
                "blog:post_detail", year=year, month=month, day=day, slug=slug
            )
    else:
        form = CommentForm()
    return render(
        request,
        "blog/posts/post_detail.html",
        {"post": post, "form": form},
    )


def about(request):
    return render(request, "blog/about.html")


from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            subject = f"Contact Form Submission from {name}"
            message_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            send_mail(
                subject,
                message_body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
            )
            return render(request, "blog/contact_success.html")
    else:
        form = ContactForm()
    return render(request, "blog/contact.html", {"form": form})
