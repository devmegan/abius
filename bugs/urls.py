from django.urls import path
from . import views

urlpatterns = [
    path('', views.bugs, name='bugs'),
    path('report_bug/', views.report_bug, name="report_bug"),
    path('delete_bug/<int:bug_id>/', views.delete_bug, name="delete_bug"),
    path('toggle_status/<int:bug_id>/', views.toggle_status, name="toggle_status"),
    path('edit_bug_description/<int:bug_id>/', views.edit_bug_description, name="edit_bug_description"),
    path('edit_bug_name/<int:bug_id>/', views.edit_bug_name, name="edit_bug_name"),
    path('update_urgency/<int:bug_id>/<direction>/', views.update_urgency, name="update_urgency"),
]
