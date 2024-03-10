from .views import *
from django.urls import path
urlpatterns=[
    path("",home,name="home"),
    path("aboutUs/",about_us,name="about_us"),
    path('ourImpact/', our_impact, name='our_impact'),
    path('ourApproach/', our_approach, name='our_approach'),
    path('corporatePartnerships/', c_p, name='c_p'),
    path('volunteering/', vol, name='vol'),
    path('blog/', blog, name='blog'),
    path('contactUs/', contact_us, name='contact_us'),
]
