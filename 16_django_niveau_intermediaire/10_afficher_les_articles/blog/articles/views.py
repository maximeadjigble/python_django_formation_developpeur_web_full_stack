from django.shortcuts import render
from django.http import HttpResponse

from .models import Article

def articles_view(request):
    articles = Article.objects.all().order_by('-date_publication')
    return render(request, 'articles/list.html', context={'articles': articles})

def article_view(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/detail.html', context={"article": article})