from django.contrib import admin
from .models import CustomUser
# from django.contrib.auth.admin import UserAdmin
# # Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number',"last_login","date_joined","is_active")

# admin.site.register(CustomUser)