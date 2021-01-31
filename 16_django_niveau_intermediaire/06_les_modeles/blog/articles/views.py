from django.shortcuts import render
from django.http import HttpResponse

from .db_articles import articles

def articles_view(request):
    return render(request, 'articles/list.html', context={'articles': articles})

def article_view(request, slug):
    for article in articles:
        if article["slug"] == slug:
            return render(request, 'articles/detail.html', context={'article': article})
    return HttpResponse("Aucun article correspondant")