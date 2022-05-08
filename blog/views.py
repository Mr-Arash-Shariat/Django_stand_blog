from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment, Message
from django.core.paginator import Paginator
from .forms import ContactUsForm, MessageForm



def posts_detail(request, slug):
    posts = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body, post=posts, user=request.user, parent_id=parent_id)

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


def search(request):
    q = request.GET.get('q')
    posts = Post.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    pagiantor = Paginator(posts, 4)
    objects_list = pagiantor.get_page(page_number)

    context = {
        'posts': objects_list,
    }

    return render(request, 'blog/posts_list.html', context)


def contact_us(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page:home')
    else:
        form = MessageForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/contact_us.html', context)