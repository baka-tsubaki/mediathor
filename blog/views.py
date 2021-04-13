from django.shortcuts import render, get_list_or_404 
from .models import *


def home(request):
    articles = Article.objects.all().order_by('-created')
    context = {
        'main': 'MediaThor Mag',
        'title': 'MediaThor Mag',
        'articles': articles,
    }
    
    return render(request, 'home.html', context)


def post(request, slug):
    articles = Article.objects.filter(slug=slug)
    context = {
        'title': 'post-page',
        'articles': articles,
        
    }
    return render(request, 'post.html', context)