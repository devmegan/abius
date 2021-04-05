from django.shortcuts import render, HttpResponse

# Views for Home App below


def index(request):
    """ view returns index page """
    return HttpResponse("🐛🐛🐛 I am surrounded by bugs. 🐛🐛🐛")
