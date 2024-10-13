from django.shortcuts import render
from django.http import HttpResponse
def infomain(request):
    return HttpResponse("<h4>infomain</h4>")
def definfo(request):
    return HttpResponse("<h4>info</h4>")
