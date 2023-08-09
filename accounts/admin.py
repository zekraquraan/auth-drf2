from django.contrib import admin
from .models import CustomUser

from django.contrib.auth.admin import UserAdmin
class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        ('Auth Info',{'fields' : ('username','email','password1', 'password2')}),
        ('Personal Information',{'fields' :('first_name','last_name','phone_number') })
    )
admin.site.register(CustomUser,CustomUserAdmin)

