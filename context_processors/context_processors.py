from blog.models import Post, Category



def recent_posts(request):
    recent_posts = Post.objects.order_by('-created')[:4]

    return {"recent_posts": recent_posts}


def recent_categories(request):
    recent_categories = Category.objects.all()

    return {"recent_categories": recent_categories}
