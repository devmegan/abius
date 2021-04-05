from django.shortcuts import render, HttpResponse
from .models import Bug

# Views for Home App below


def bugs(request):
    """ view returns bugs page """
    bugs = Bug.objects.all().order_by("urgency")
    context = {
        'bugs': bugs,
    }
    return render(request, 'bugs/bugs.html', context)
