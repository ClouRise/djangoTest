from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h4>main</h4>")
def secondPage(request):
    return HttpResponse("<h4>second page</h4>")