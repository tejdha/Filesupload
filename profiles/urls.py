from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('profile/',addprofile,name='profile'),
    path('view/',viewprofiles,name='view'),
    path('search/',searchprofiles,name='search'),
    path('searchit/<str:date>',searchit,name='searchit'),
]