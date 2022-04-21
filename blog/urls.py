from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('detail/<slug:slug>', views.posts_detail, name='detail'),
    path('list/', views.posts_list, name='list'),
]
