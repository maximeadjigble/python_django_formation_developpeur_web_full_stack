from django.http import HttpResponse

def home_view(request):
    return HttpResponse('Hello World!')

def contact_view(request):
    return HttpResponse('Contactez nous')