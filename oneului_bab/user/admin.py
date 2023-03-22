from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'name', 'nickname', 'birth_date', 'is_staff', 'is_active')
    list_filter = ('email', 'name', 'nickname', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'nickname', 'birth_date')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'nickname', 'birth_date', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'name', 'nickname')
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
