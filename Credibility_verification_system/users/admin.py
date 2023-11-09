from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Statement, Verdict


class CustomUserAdmin(UserAdmin):
    # Define the fields you want to display in the user list view
    list_display = ('username', 'email', 'first_name', 'last_name','gender','country' ,'password')

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

class StatementAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'created_at', 'statement')

# Custom admin class for Verdict
class VerdictAdmin(admin.ModelAdmin):
    list_display = ('form_id', 'statement_id', 'Statement_verdict', 'predicted_probability')

# Register the Statement and Verdict models with their respective admin classes
admin.site.register(Statement, StatementAdmin)
admin.site.register(Verdict, VerdictAdmin)

# Configure Jazzmin settings
# class MyAdminSite(JazzminSettings):
#     site_title = "Admin Panel"
#     site_header = "Admin Panel"
#     site_logo = "images/logo3.png"
#     site_brand = "CVS"
#     show_sidebar = True
#     navigation_expanded = True
#     hide_apps = []
#     hide_models = []
#     order_with_respect_to = ["auth", "Users", "Verifications"]
#     icons = {
#         "auth": "fas fa-users-cog",
#         "auth.user": "fas fa-user",
#         "auth.Group": "fas fa-users",
#         "Users.users": "fas fa-user",
#         "Users.statement": "fas fa-file-text",
#         "Users.verdict": "fas fa-clipboard-check",
#     }
#     default_icon_parents = "fas fa-chevron-circle-right"
#     default_icon_children = "fas fa-circle"

# # Create a custom admin site for Jazzmin
# admin.site = MyAdminSite()
