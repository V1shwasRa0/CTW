from .views import *
from django.urls import path
urlpatterns=[
    path("",home,name="home"),
    path("about_us",about_us,name="about_us"),
    path('our_approach', our_approach, name='our_approach'),
    path('our-impact/', our_impact, name='our_impact'),
    path('c_p/', c_p, name='c_p'),
    path('vol', vol, name='vol'),
    path('blog', blog, name='blog'),
    path('contact_us', contact_us, name='contact_us'),
]
