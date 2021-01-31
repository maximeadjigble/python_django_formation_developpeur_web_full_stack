from django.shortcuts import render
from django.http import HttpResponse

def utilisateurs_view(request):
    return HttpResponse("Page d'utilisateurs")