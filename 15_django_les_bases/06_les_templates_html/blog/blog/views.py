from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    # return HttpResponse('Hello World!')
    return render(request, 'home.html')

def contact_view(request):
    # return HttpResponse('Contactez nous')
    return render(request, 'contact.html')