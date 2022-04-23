from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.core.paginator import Paginator



def posts_detail(request, slug):
    posts = get_object_or_404(Post, slug=slug)

    context = {
        'posts': posts,
    }

    return render(request, 'blog/posts_detail.html', context)


def posts_list(request):
    posts = Post.objects.all().order_by('-created',)
    page_number = request.GET.get('page')
    paginator = Paginator(posts, 4)
    objects_list = paginator.get_page(page_number)

    context = {
        'posts': objects_list,
    }

    return render(request, 'blog/posts_list.html', context)


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    posts = category.posts.all()

    context = {
        'posts': posts,
    }
    return render(request, 'blog/posts_list.html', context)