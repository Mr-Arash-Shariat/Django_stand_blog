from django.shortcuts import render, get_object_or_404
from .models import Post



def posts_detail(request, slug):
    posts = get_object_or_404(Post, slug=slug)

    context = {
        'posts': posts,
    }

    return render(request, 'blog/posts_detail.html', context)


def posts_list(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'blog/posts_list.html', context)
