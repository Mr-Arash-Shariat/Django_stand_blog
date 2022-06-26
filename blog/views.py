from turtle import title
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment, Message
from django.core.paginator import Paginator
from .forms import MessageForm
from django.views.generic import ListView, DetailView, FormView
from . import mixins as my_mixins


class PostDetail(my_mixins.CustomLoginRequiredMixin, DetailView):
    model = Post
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Post.objects.all(), slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['comment'] = Comment.objects.all()
        context['form'] = Comment()
        return context


class PostList(ListView):
    queryset = Post.objects.filter(status=True).order_by('-created',)
    paginate_by = 4


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


class ContactUsView(FormView):
    template_name = "blog/contact_us.html"
    form_class = MessageForm
    success_url = "/"


    def form_valid(self, form):
        form_data = form.cleaned_data
        Message.objects.create(**form_data)

        return super().form_valid(form)