from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Count

from .models import Post
from .forms import CommentForm


def Post_list(request):
    # comment_count added using annotate
    qs = Post.objects.annotate(comment_count=Count("comments")).order_by("-created_at")

    paginator = Paginator(qs, 5)  # 5 posts per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "blog/post_list.html", {
        "posts": page_obj,        # keep your template loop working
        "page_obj": page_obj,
    })


def Post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by("-created_at")

    # small "recent posts" list for sidebar
    recent_posts = Post.objects.exclude(pk=post.pk).order_by("-created_at")[:5]

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", slug=post.slug)
    else:
        form = CommentForm()

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "form": form,
        "recent_posts": recent_posts,
    })