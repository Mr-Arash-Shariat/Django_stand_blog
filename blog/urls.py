from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('detail/<slug:slug>', views.PostDetail.as_view(), name='detail'),
    path('list/', views.PostList.as_view(), name='list'),
    path('category/<int:pk>', views.category_detail, name='category_detail'),
    path('search/', views.search, name='search-posts'),
    path('contact-us/', views.ContactUsView.as_view(), name='contact_us'),
]
