from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

class data(models.Model):
    type = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date = models.DateField()
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    for_whom = models.CharField(max_length=100)

class projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    for_whom = models.CharField(max_length=100)
    deadline = models.DateField()