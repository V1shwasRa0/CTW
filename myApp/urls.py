from .views import *
from django.urls import path
urlpatterns=[
    path("",home,name="home"),
    path("about_us",about_us,name="about_us"),
    path("home",home,name="home"),
    path('ourImpact/', our_impact, name='our_impact'),
]