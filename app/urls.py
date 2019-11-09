from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_people, name='list_people'),
]
