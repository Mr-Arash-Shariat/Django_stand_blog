from django.shortcuts import render
from blog.models import Post, Category



def home_page(request):
    posts = Post.objects.filter(status=True)
    category = Category.objects.all()
    recent_posts = Post.objects.all().order_by('-created')[:3]

    context = {
        "posts": posts,
        "categories": category,
    }

    return render(request, "home/index.html", context)
