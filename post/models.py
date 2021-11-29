from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_pictures/', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    timestanp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestanp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
