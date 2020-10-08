from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from myonlineshop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponApplyForm
from django.contrib import messages
from django.http import HttpResponseRedirect


@require_POST
def cart_add(request, product_id):
    url = request.META.get('HTTP_REFERER') #get last url
    
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    
    
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'],
                 size_cloth= cd['size_cloth']),
                 
        messages.success(request, "Item added to Cart.")
    

 
    
                 
                 

    
    return HttpResponseRedirect(url)
        
                 
    # return redirect('myonlineshop:product_detail')




@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
                            'quantity': item['quantity'],
                            'override': True}) 
                           

 
    coupon_apply_form = CouponApplyForm()                        
    return render(request, 'cart/detail.html', {'cart': cart, 'coupon_apply_form': coupon_apply_form})

def checkout(request):
    return render(request, 'cart/checkout.html', {})
