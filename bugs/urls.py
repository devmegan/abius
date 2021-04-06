from django.urls import path
from . import views

urlpatterns = [
    path('', views.bugs, name='bugs'),
    path('bug_detail/<int:bug_id>', views.bug_detail, name="bug_detail"),
    path('delete_bug/<int:bug_id>', views.delete_bug, name="delete_bug"),
    path('toggle_status/<int:bug_id>', views.toggle_status, name="toggle_status")
]
