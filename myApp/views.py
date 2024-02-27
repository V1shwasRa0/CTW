from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"sample.html")

def home_view(request):
    return render(request,"home.html")

def about_us(request):
    return render(request,"aboutus.html")

def our_impact(request):
    return render(request, 'ourImpact.html')
