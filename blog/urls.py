from django.urls import path
from .views import posts_detail


app_name = 'blog'

urlpatterns = [
    path('detail/<int:pk>', posts_detail, name='detail')
]
