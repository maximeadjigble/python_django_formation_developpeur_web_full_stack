from django.shortcuts import render
from django.http import HttpResponse

from .db_articles import articles

def articles_view(request):
    return render(request, 'articles/list.html', context={'articles': articles})

def article_view(request, slug):
    # return HttpResponse(slug)
    for article in articles:
        if article["slug"] == slug:
            return HttpResponse(article["contenu"])
    return HttpResponse("Aucun article correspondant")