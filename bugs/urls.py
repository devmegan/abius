from django.urls import path
from . import views

urlpatterns = [
    path('', views.bugs, name='bugs'),
    path('bug_detail/<int:bug_id>', views.bug_detail, name="bug_detail")
]
