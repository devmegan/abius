from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Bug

# Views for Home App below


def bugs(request):
    """ view returns bugs page """
    bugs = Bug.objects.all().order_by("urgency")
    context = {
        'bugs': bugs,
    }
    return render(request, 'bugs/bugs.html', context)


def bug_detail(request, bug_id):
    """ view to inspect bug in detail """
    bug = Bug.objects.get(pk=bug_id)

    context = {
        'bug': bug,
    }
    return render(request, 'bugs/bug_detail.html', context)

