from django.urls import path
from app2.views import *
app2_name='tara'
urlpatterns=[
    path('virat/', virat,name='virat'),
]