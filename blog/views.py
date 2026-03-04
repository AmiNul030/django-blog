from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import CommentForm

def Post_list(request):
    posts=Post.objects.all().order_by("-created_at")
    return render(request,'blog/post_list.html',{'posts':posts})

def Post_detail(request,slug):
    post=get_object_or_404(Post,slug=slug)
    comments=Post.comments.all().order_by("-created_at")

    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',slug=post.slug)
    else:
        form=CommentForm()
    return render(request,'blog/post_detail.html',
                  {'post':post,'comments':comments,'form':form})

