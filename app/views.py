# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from models import *

def index(request):
    return HttpResponse("<h1>Hey what's up!<h1>")
def app(request):
    return HttpResponse("Hello world")

def UniversityName(request, University_ID):
    return HttpResponse("%s"%(University.objects.get(pk=University_ID)))
# Create your views here.
