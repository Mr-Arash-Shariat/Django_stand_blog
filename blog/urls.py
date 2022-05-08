from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('detail/<slug:slug>', views.posts_detail, name='detail'),
    path('list/', views.posts_list, name='list'),
    path('category/<int:pk>', views.category_detail, name='category_detail'),
    path('search/', views.search, name='search-posts'),
    path('contact-us/', views.contact_us, name='contact_us'),
]
