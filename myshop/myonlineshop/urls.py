from django.urls import path
from . import views


app_name = 'myonlineshop'

urlpatterns = [
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('home', views.index, name='index'),
    path('selectcurrency', views.selectcurrency, name='selectcurrency'),
    path('picture_x', views.picture, name='picture'),
    path('contact', views.contact, name='contact'),
    path('checkout', views.checkout, name='checkout'),
    
    path('categorie', views.categorie, name='categorie'),
    path('search', views.post_search, name='post_search'),
    path('store', views.product_list, name='product_list'),

   
    # path('addcomment/<int:id>', views.addcomment, name='addcomment'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    


]
