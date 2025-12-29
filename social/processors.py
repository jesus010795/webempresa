from .models import Links


def context_dict(request):
    context = {link.key: link.url for link in Links.objects.all()}
    return context
