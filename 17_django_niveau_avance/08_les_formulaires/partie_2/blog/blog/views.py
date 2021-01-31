from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ContactForm

def home_view(request):
    # return HttpResponse('Hello World!')
    return render(request, 'home.html')

def contact_view(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        print(form)
        return HttpResponseRedirect(reverse('remerciements'))
    return render(request, 'contact.html', {"form": form})

def remerciements_view(request):
    return HttpResponse("Merci de nous avoir contacté")
