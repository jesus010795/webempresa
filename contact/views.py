from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import Contact


# Create your views here.
def contact(request):
    contact_form = Contact()

    if request.method == "POST":
        contact_form = Contact(data=request.POST)
        print(contact_form)
        if contact_form.is_valid():
            name = contact_form.cleaned_data["name"]
            email = contact_form.cleaned_data["email"]
            content = contact_form.cleaned_data["content"]
            # "Enviar email"
            return redirect(reverse("contact") + "?ok")
        else:
            contact_form = Contact()

    return render(request, "contact/contact.html", {"form": contact_form})
