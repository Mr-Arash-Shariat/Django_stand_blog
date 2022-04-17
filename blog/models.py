from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=50, unique_for_date="publish")
    category = models.ManyToManyField(Category)
    body = models.TextField()
    image = models.ImageField(upload_to='images/posts')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
