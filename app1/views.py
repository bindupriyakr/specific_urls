from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def msd(request):
    return HttpResponse('<h3>msd is the best captain</h3>')