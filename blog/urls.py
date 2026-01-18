from codecs import namereplace_errors

from django.urls import path
from . import views
urlpatterns=[
    path('', views.index,name ='blog'),
]