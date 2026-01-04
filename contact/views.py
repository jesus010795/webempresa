from django.shortcuts import render
from .forms import Contact


# Create your views here.
def contact(request):
    contact_form = Contact()
    return render(request, "contact/contact.html", {"form": contact_form})
