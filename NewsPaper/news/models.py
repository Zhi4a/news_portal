from django.db import models
from django.contrib.auth.models import User


class Autor(models.Model):
    rating = models.FloatField()

    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Category(models.Model):
    category = models.CharField(max_length=255, unique=True)


article = 'AR'
news = 'NW'

TYPE = [
    (article, 'Статья'),
    (news, 'Новость'),
]


class Post(models.Model):
    _type = models.CharField(max_length=2, choices=TYPE, default=news)
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.FloatField()

    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    rating = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
