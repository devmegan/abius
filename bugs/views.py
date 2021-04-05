from django.shortcuts import render, HttpResponse

# Views for Home App below


def bugs(request):
    """ view returns bugs page """
    return HttpResponse("🐛🐛🐛 I am surrounded by bugs. 🐛🐛🐛")
