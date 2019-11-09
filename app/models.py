from django.conf import settings
from django.db import models
from django.utils import timezone


class People(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    pathromic = models.CharField(max_length=200)
    friends = models.CharField(max_length=100)

    def fullname(self):
        return '{} {} {}'.format(self.firstname, self.lastname, self.pathromic)

    def __str__(self):
        return self.fullname()