from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
# Register your models here.
class CustomUserAdmin(UserAdmin) :
    model = User
    list_display = ['pk', 'email', 'username']
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {'fields': ('email', 'username', 'address')}),
    # )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('address',)}),
    )


admin.site.register(User, CustomUserAdmin)