from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .form import CustomUser, Create, Change

# Register your models here.

class Admin(UserAdmin):
    add_form = Create
    form = Change
    model = CustomUser
    list_display = ['first_name', 'last_name', 'age', 'birth_year']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', )}),
    )

admin.site.register(CustomUser, Admin)