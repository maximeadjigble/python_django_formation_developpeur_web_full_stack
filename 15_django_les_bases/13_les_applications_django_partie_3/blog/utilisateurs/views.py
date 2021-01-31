from django.shortcuts import render
from django.http import HttpResponse

def utilisateurs_view(request):
    # return HttpResponse("Page d'utilisateurs")
    return render(request, 'utilisateurs/liste.html')

def creer_view(request):
    return HttpResponse("Page de création d'utilisateurs")