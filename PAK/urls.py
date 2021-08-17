from django.urls import path
from PAK.views import *

app_name='PAK'

urlpatterns=[
    path('PAKISTAN/',PAKISTAN,name='PAKISTAN'),
]