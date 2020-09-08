from django.urls import path
from . import views


app_name = 'myonlineshop'

urlpatterns = [
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('index', views.index, name='index'),
    path('picture_x', views.picture, name='picture'),
    path('contact', views.contact, name='contact'),
    path('checkout', views.checkout, name='checkout'),
    path('cart', views.cart, name='cart'),
    path('categorie', views.categorie, name='categorie'),
    path('store', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail')

]
