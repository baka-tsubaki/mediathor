from django.shortcuts import render, get_list_or_404 
from .models import *
from .forms import *
from django.shortcuts import HttpResponseRedirect

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


def contact(request):
    success = 'formulaire soumis correctement'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'form': form, 'success': success})
    
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

