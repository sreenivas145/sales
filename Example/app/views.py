from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")

@login_required
def showMobile(request):
    return render(request,"mobiles.html")

@login_required
def showLaptops(request):
    return render(request,"laptops.html")

@login_required
def showTabs(request):
    return render(request,"tabs.html")


def afterlogin(request):
    return showIndex(request)