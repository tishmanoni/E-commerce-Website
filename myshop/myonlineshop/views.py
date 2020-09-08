from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import Category, Product
from cart.forms import CartAddProductForm

# Create your views here.


def home(request):
    #return HttpResponse("<h1>Homepage</h1>")
    usx = myUser.objects.all()
    return render(request, 'home.html', {'usx':usx})


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})


# product.html
# contact
# checkoutcategorie
# cart

def contact(request):
    return render(request, 'contact.html', {})


def cart(request):
    return render(request, 'cart.html', {})

def checkout(request):
    return render(request, 'checkout.html', {})

def categorie(request):
    return render(request, 'categorie.html', {})

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


def product_list (request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/store.html', {'category':category, 'categories':categories, 'products': products})      

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})  
    
    