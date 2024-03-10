from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"home.html")

def about_us(request):
    return render(request,"aboutus.html")

def our_approach(request):
    return render(request, 'our_approach.html')

def our_impact(request):
    return render(request, 'ourImpact.html')

def c_p(request):
    return render(request, 'c_p.html')

def vol(request):
    return render(request, 'vol.html')

def blog(request):
    return render(request, 'blog.html')

def contact_us(request):
    return render(request, 'contact_us.html')
