from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import Category, Product, Review
from cart.forms import CartAddProductForm
from django.contrib.auth.decorators import login_required

from .forms import ReviewForm, SearchForm
from django.contrib.postgres.search import SearchVector
from django.contrib import messages
from django.http import HttpResponseRedirect


from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger


# Create your views here.


def home(request):
    #return HttpResponse("<h1>Homepage</h1>")
    usx = myUser.objects.all()
    return render(request, 'home.html', {'usx':usx})


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    if not request.session.has_key('currency'):
        request.session['currency'] = settings.DEFAULT_CURRENCY

   
    
    return render(request, 'index.html', {'products':products, 'categories':categories, 'settings':settings})

def selectcurrency(request):
    lasturl = request.META.get('HTTP_REFERER')
    if request.method == 'POST':  # check post
        request.session['currency'] = request.POST['currency']
    return HttpResponseRedirect(lasturl)


# product.html
# contact
# checkoutcategorie
# cart

def contact(request):
    categories = Category.objects.all()
    return render(request, 'shop/product/contact.html', {'categories':categories})


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
    my_products = Product.objects.filter(available=True)
    # my_products = Product.objects.all()
    paginator = Paginator(my_products, 6) # 3 posts in each page
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
         # If page is not an integer deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        my_products = my_products.filter(category=category)
        paginator = Paginator(my_products, 3) # 3 posts in each page
        page = request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            products = paginator.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            products = paginator.page(paginator.num_pages)
        
    return render(request, 'shop/product/store.html', {'category':category, 'categories':categories, 'my_products': my_products, 'page':page, 'products':products})      

from .recommender import Recommender
def product_detail(request, id, slug):
    
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    
    
  
    comments = product.review.filter(active=True)
    new_comment = None
    user = request.user
    if request.method == 'POST':
        # A comment was posted
        comment_form = ReviewForm(data=request.POST)
        if comment_form.is_valid():
            data = Review()
            data.name = comment_form.cleaned_data['name']
            data.email = comment_form.cleaned_data['email']
            data.body = comment_form.cleaned_data['body']
            product = product
            data.product = product
            current_user = request.user
            data.user_id = current_user.id
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.product = product
            new_comment = data
            # Save the comment to the database
            new_comment.save()
            messages.success(request, "Your review has been sent. Thank you")
    else:
        comment_form = ReviewForm()
   
    return render(request,'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form, 'comments': comments,'new_comment': new_comment, 'comment_form': comment_form, 'recommended_products': recommended_products })  

# def addcomment(request, id):
#     url = request.META.get('HTTP_REFERER') #get last url
#     # return HttpResponse(url)
#     if request.method == "POST": #check Post
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             data = Review() # create relation to model
#             data.name = form.cleaned_data['name']
#             data.email = form.cleaned_data['email']
#             data.body = form.cleaned_data['body']
#             data.rate = form.cleaned_data['rate']
#             data.ip = request.META.get('REMOTE_ADDR')
#             data.product_id = id
#             current_user = request.user
#             data.user_id = current_user.id
#             data.save() #save data to table
#             messages.success(request, "Your review has been sent. Thank you")
#             return HttpResponseRedirect(url)
#     return HttpResponseRedirect(url)


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    categories = Category.objects.all()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.annotate(search=SearchVector('name', 'price'),   ).filter(search=query)
    return render(request,  'shop/product/search.html', {'form': form, 'query': query,'results': results, 'categories':categories})
   
    
