from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all(),
        'page_title': 'My blog',
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
