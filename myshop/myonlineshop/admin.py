from django.contrib import admin
from .models import Category, Product, Review

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated', 'new', 'best', 'sale', 'Featured', 'New_arrivals', 'Premium', 'recomended']
    # list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available', 'new', 'sale', 'best','Featured', 'New_arrivals', 'Premium', 'recomended']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'user','email', 'product', 'created', 'active')
    # list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


