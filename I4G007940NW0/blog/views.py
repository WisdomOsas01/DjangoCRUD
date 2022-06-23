from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Post
from django.views.generic import UpdateView, CreateView, DeleteView, ListView, DetailView


# Create your views here.

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


class PostUpdateView(UpdateView):
    model = Post

    fields = "__all__"

    success_url = reverse_lazy("blog: all")


class PostDeleteView(DeleteView):
    model = Post

    fields = "__all__"

    success_url = reverse_lazy("blog: all")


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post
