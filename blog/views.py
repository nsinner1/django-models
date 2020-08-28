from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Blog


# Create your views here.
# class HomePageView(TemplateView):
#     template_name = 'home.html'

# class PostDetailPageView(ListView):
#     template_name = 'post_detail.html'
#     model = Blog

class HomePageView(ListView):
    template_name = 'home.html'
    model = Blog


class PostDetailPageView(DetailView):
    template_name = 'post_detail.html'
    model = Blog