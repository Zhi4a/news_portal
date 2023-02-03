from django.db import models
from django.contrib.auth.models import User
from .res import TYPE


class Autor(models.Model):
    rating = models.FloatField(default=0)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        self.rating = 0
        for post in Post.objects.filter(author=self):
            self.rating += post.rating * 3
            for comment in Comment.objects.filter(post=post):
                self.rating += comment.comment_rating
        for comment in Comment.objects.filter(user=self.user):
            self.rating += comment.comment_rating
        self.save()


class Category(models.Model):
    category = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    _type = models.CharField(max_length=2, choices=TYPE, default='NW')
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.FloatField(default=0)

    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def preview(self):
        return self.text[:124:1] + '...'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    rating = models.FloatField(default=0)
    time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
