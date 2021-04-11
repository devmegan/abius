from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Bug
from .forms import BugForm

# Views for Home App below

@login_required
def bugs(request):
    """ view returns bugs page """

    add_bug_form = BugForm()

    user = get_object_or_404(User, username=request.user)
    if user.is_superuser:
        bugs = Bug.objects.all().order_by("urgency")
        urgent_bugs = bugs.filter(urgency=3)
        important_bugs = bugs.filter(urgency=2)
        annoying_bugs = bugs.filter(urgency=1)
    else: 
        return redirect('report_bug')
    # handles add_bug form
    if request.method == 'POST':
        if 'description' in request.POST:
            add_bug_form = BugForm(request.POST)
            if add_bug_form.is_valid():
                add_bug_form.save()
            return redirect('bugs')
    context = {
        'bugs': bugs,
        'urgent_bugs': urgent_bugs,
        'important_bugs': important_bugs,
        'annoying_bugs': annoying_bugs,
        'add_bug_form': add_bug_form
    }
    return render(request, 'bugs/bugs.html', context)


def report_bug(request):
    """ view to inspect bug in detail """
    
    add_bug_form = BugForm()
    
    if request.method == 'POST':
        if 'description' in request.POST:
            add_bug_form = BugForm(request.POST)
            if add_bug_form.is_valid():
                new_bug = add_bug_form.save()
                messages.info(
                    request, f'"{new_bug.name}" has been reported to the bug squad.'
                )
                return redirect('index')
    
    context = {
        'add_bug_form': add_bug_form
    }
    return render(request, 'bugs/report_bug.html', context)


def toggle_status(request, bug_id):
    """ toggle the complete/incomplete status of bugs """
    bug = get_object_or_404(Bug, id=bug_id)
    bug.status = not bug.status  # invert bug status
    bug.save()
    return redirect('bugs')


def update_urgency(request, bug_id, direction):
    """ increase or decrease bug urgency """
    bug = get_object_or_404(Bug, id=bug_id)
    if direction == "inc":
        bug.urgency += 1
    else:
        bug.urgency -= 1
    bug.save()
    return redirect('bugs')


def delete_bug(request, bug_id):
    """ view will delete bug forever """
    bug = get_object_or_404(Bug, id=bug_id)
    bug.delete()
    return redirect('bugs')
