from django import forms

class ContactForm(forms.Form):
    # https://docs.djangoproject.com/en/3.1/ref/forms/fields/
    nom = forms.CharField(max_length=200)
    prenom = forms.CharField(max_length=200)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)