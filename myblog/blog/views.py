from django.shortcuts import render, redirect
from .models import Comment, Post
from .forms import *
# Create your views here.

def front(request):
    posts= Post.objects.all()
    return render(request, 'blog/front.html', {'posts': posts})

def post(request, slug):
    post= Post.objects.get(slug=slug)

    if request.method == 'POST':
        form= CommentForm(request.POST)

        if form.is_valid():
            comment= form.save(commit= False)
            comment.post= post
            comment.save()

            return redirect('post', slug=post.slug)
    else:
        form= CommentForm()

    return render(request, 'blog/post.html', {'post': post, 'form': form })    



