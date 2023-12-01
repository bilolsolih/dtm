from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.user import User


class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'get_full_name', 'phone_number', 'type']
    list_display_links = ['id', 'get_full_name', 'phone_number', 'type']
    list_filter = ['type', 'gender', 'is_active', 'is_verified']
    fieldsets = (
        (None, {'fields': ('phone_number', 'username', 'email', 'is_verified', 'is_active')}),
        ('Personal Info', {'fields': ('first_name', 'middle_name', 'last_name', 'nickname', 'photo', 'birthdate', 'gender')}),
        ('Permissions', {'fields': ('type', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': ('phone_number', 'username', 'email', 'first_name', 'middle_name', 'last_name', 'nickname', 'birthdate', 'photo', 'password1', 'password2')
            }
        ),
    )
    search_fields = ['first_name', 'last_name', 'middle_name', 'username', 'phone_number']
    readonly_fields = ['last_login', 'created', 'updated']
    ordering = ('-created',)


admin.site.register(User, CustomUserAdmin)
