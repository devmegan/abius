from django.urls import path
from . import views

urlpatterns = [
    path('', views.bugs, name='bugs'),
]
