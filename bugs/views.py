from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Bug

# Views for Home App below


def bugs(request):
    """ view returns bugs page """
    bugs = Bug.objects.all().order_by("urgency")
    urgent_bugs = bugs.filter(urgency=3)
    important_bugs = bugs.filter(urgency=2)
    annoying_bugs = bugs.filter(urgency=1)
    context = {
        'bugs': bugs,
        'urgent_bugs': urgent_bugs,
        'important_bugs': important_bugs,
        'annoying_bugs': annoying_bugs,
    }
    return render(request, 'bugs/bugs.html', context)


def bug_detail(request, bug_id):
    """ view to inspect bug in detail """
    bug = Bug.objects.get(id=bug_id)

    context = {
        'bug': bug,
    }
    return render(request, 'bugs/bug_detail.html', context)


def toggle_status(request, bug_id):
    """ toggle the complete/incomplete status of bugs """
    bug = get_object_or_404(Bug, id=bug_id)
    bug.status = not bug.status  # invert bug status
    bug.save()
    return redirect('bugs')


def delete_bug(request, bug_id):
    """ view will delete bug forever """
    bug = get_object_or_404(Bug, id=bug_id)
    bug.delete()
    return redirect('bugs')
