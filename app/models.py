# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class University(models.Model):
    Name = models.CharField(max_length=30)
    Acceptancerate = models.CharField(max_length=20)
    TuitionFees = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    def __str__(self):
        return self.Name + " - " + self.Acceptancerate
class Departnemnt(models.Model):
    University = models.ForeignKey(University, on_delete=models.CASCADE)
    FacultyName = models.CharField(max_length=25)


