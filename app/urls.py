from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_people, name='list_people'),
    path('', include('social_django.urls')),
]
