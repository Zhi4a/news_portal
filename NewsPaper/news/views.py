from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-time'
    template_name = 'posts.html'
    context_object_name = 'posts'


class ProductDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
