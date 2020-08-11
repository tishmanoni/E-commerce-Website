from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
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

def picture(request):
    #return HttpResponse("<h4>It works</h4>")
    if request.method == 'POST' and request.FILES['my_pics']:
        dnm = "if block"
        myfile = request.FILES['my_pics']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        the_url_of_uploaded_file = fs.url(filename)
        return render(request,"picture.html",{'the_url_of_uploaded_file': the_url_of_uploaded_file})
    
    else:
        dnm = "else block"
        return render(request,"picture.html",{"fnme":dnm})

        
    
    