from .views import *
from django.urls import path
urlpatterns=[
    path("",home,name="home"),
    path("about-us/",about_us,name="about_us"),
    path('our-approach/', our_approach, name='our_approach'),
    path('our-impact/', our_impact, name='our_impact'),
    path('partnerships/', c_p, name='c_p'),
    path('volunteering/', vol, name='vol'),
    path('blog/', blog, name='blog'),
    path('contact/', contact_us, name='contact_us'),
]
