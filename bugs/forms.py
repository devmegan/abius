from django import forms
from .models import Bug


class BugForm(forms.ModelForm):
    # form will create a new Bug object
    class Meta:
        model = Bug
        fields = ['name', 'description', 'urgency']
