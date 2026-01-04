from django import forms


class Contact(forms.Form):
    name = forms.CharField(label="Nombre")
    email = forms.EmailField(label="Email")
    content = forms.CharField(label="Contenido", widget=forms.Textarea)
