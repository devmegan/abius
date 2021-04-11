from django.shortcuts import render, HttpResponse, redirect

# Views for Home App below


def index(request):
    """ view returns index page """
    
    return render(request, 'home/index.html')
