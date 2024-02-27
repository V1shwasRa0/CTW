from .views import *
from django.urls import path
urlpatterns=[
    path("",home,name="home"),
    path("about_us",about_us,name="about_us"),
    path("home_view",home_view,name="home_view"),
    path('ourImpact/', our_impact, name='our_impact'),
]
