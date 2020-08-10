from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Product, myUser
# Create your views here.


def home(request):
    #return HttpResponse("<h1>Homepage</h1>")
    usx = myUser.objects.all()
    return render(request, 'home.html', {'usx':usx})

def about(request, *args, **kwargs):
    #return HttpResponse("<h1>About Us</h1>")

    return render(request, "about.html", {})

def contact(request, *args, **kwargs):
    return HttpResponse("<h1>Contact Us</h1>")

def dashboard(request, *args, **kwargs):
    return HttpResponse("<h1>Welcome to your dashboard</h1>")

def pictures(request):
    #return HttpResponse("<h4>It works</h4>")
    if request.method == "POST":
        p_file = request.FILES['my_pics']
        fx = FileSystemStorage().save(p_file.name, p_file)
        
    
    return render (request, "pictures.html")