from django.urls import path
from IND.views import *

app_name='IND'

urlpatterns=[
    path('INDIA/',INDIA,name='INDIA'),
    ]