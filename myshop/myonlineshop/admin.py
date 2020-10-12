from django.contrib import admin
from .models import Category, Product, Review


# Register your models here.

# class VariationInline(admin.TabularInline):
#     model = Variation
#     raw_id_fields = ['product']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image','price', 'available', 'created', 'updated', 'best', 'sale', 'Featured', 'New_arrivals', 'Premium', 'super_offer', 'super_offer2']
    # list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available', 'sale', 'best','Featured', 'New_arrivals', 'Premium', 'super_offer', 'super_offer2']
    prepopulated_fields = {'slug': ('name',)}
    # inlines = [VariationInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'user','email', 'product', 'created', 'active')
    # list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')



