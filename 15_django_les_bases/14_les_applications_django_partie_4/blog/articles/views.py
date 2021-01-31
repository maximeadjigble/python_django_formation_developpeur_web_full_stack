from django.shortcuts import render

from .db_articles import articles

def articles_view(request):
    return render(request, 'articles/list.html', context={'articles': articles})