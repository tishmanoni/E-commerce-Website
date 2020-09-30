from django.urls import reverse
from django.shortcuts import render, redirect

# Create your views here.

def my_payment(request):

    return render(request, 'payment/pay.html', {})

def payment_done(request):
    return render(request, 'payment/done.html')
def payment_canceled(request):
    return render(request, 'payment/canceled.html')


# def payment_process(request):
#     order_id = request.session.get('order_id')
#     order = get_object_or_404(Order, id=order_id)
#     total_cost = order.get_total_cost()
#     if request.method == 'POST':