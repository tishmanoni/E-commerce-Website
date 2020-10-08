from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo', 'country','address', 'postal_code', 'city']

