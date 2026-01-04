from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.mail import EmailMessage
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
            # "Enviar email y redireccionar
            email = EmailMessage(
                "Nuevo mensaje de contacto",
                "De {} <{}> \n Escribio:\n\n{}".format(name, email, content),
                "no-reply@inbox.mailtrap.io",
                ["jcd010795@gmail.com"],
                reply_to=[email],
            )
            try:
                email.send()
                return redirect(reverse("contact") + "?ok")
            except:
                return redirect(reverse("contact") + "?fail")

        else:
            contact_form = Contact()

    return render(request, "contact/contact.html", {"form": contact_form})
