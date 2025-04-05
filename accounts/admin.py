from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id', 'email', 'username', 'phone', 'is_staff', 'is_active')
    search_fields = ('email', 'username', 'phone')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('id',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'phone', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)