from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
class UserAdmin(UserAdmin):
    list_display =('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    search_fields = ('first_name','email')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_per_page = 25
    list_filter = ('date_joined','last_login','is_active')
    fieldsets = ()
    
admin.site.register(User,UserAdmin)  