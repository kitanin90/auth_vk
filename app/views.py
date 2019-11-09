from django.shortcuts import render
from .models import People


def list_people(request):
    personality = People.objects.all()
    return render(request, 'app/list_people.html', {'personality': personality})
