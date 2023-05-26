from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def virat(request):
    return HttpResponse('<marquee><h4>virat is best player</h4></marquee>')
