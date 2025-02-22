from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BasedUserAdmin
# Register your models here.
from . models import User

class UserAdmin(BasedUserAdmin):
    ordering = ['email']
    list_display = ['email', 'nama', 'is_staff']

    fieldsets = (
        (None, {'fields': ('email', 'nama', 'password',)}),
        ('Personal info', {'fields': ('tmp_lahir', 'tgl_lahir', 'no_hp',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),
    )

    add_fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['nama', 'email', 'password1', 'password2'],
            }
        )
    ]

admin.site.register(User, UserAdmin)