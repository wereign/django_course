from typing import Any
from django.db.models.query import QuerySet
from django.utils import timezone
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,UpdateView,DetailView,CreateView,DeleteView)

from blog.forms import PostForm,CommentForm
from blog.models import Post,Comment
# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin,ListView):

    model = Post
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    
    


        
    

