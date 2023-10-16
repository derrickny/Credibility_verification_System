from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser 
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser  # Import your custom user model

class CustomUserAdmin(UserAdmin):
    # Define the fields you want to display in the user list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'password')

    # Define the fields you want to include in the user detail view
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Names', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Customize the add user form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name','username', 'email', 'password1', 'password2'),
        }),
    )

    # Customize the search fields
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # Customize the ordering of users in the admin list view
    ordering = ('username',)

# Register your custom admin class with the CustomUser model
admin.site.register(CustomUser, CustomUserAdmin)
