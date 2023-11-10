from django.shortcuts import render


# Create your views here.

def vw_home(request, ):
    return render(request, "home_page.html")
