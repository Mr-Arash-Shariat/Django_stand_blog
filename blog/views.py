from django.shortcuts import render, get_object_or_404
from .models import Post



def posts_detail(request, pk):
    posts = get_object_or_404(Post, id=pk)

    context = {
        'posts': posts,
    }

    return render(request, 'blog/posts_detail.html', context)
