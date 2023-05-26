from django.urls import path
from app1.views import *
app1_name='tassu'
urlpatterns=[
    path('msd/', msd, name='msd'),
]
