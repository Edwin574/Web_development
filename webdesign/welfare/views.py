from django.shortcuts import render

# Create your views here.
def  home(request):
    return render(request,"home/homepage.html")
def lists(request):
    return render(request,"home/lists.html")
