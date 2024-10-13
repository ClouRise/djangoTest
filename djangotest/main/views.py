from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'main/index.html')
def secondPage(request):
    return HttpResponse("<h4>second page</h4>")