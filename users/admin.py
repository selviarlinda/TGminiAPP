from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('balance',)}),
    )
    list_display = ['username', 'email', 'balance']

admin.site.register(CustomUser, CustomUserAdmin)
