from django.contrib import admin
from main_app.models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display=('email','username','date_joined','last_login','is_staff','is_admin')
    readonly_fields=('id','date_joined','last_login')
    search_fields=('username','email')

    fieldsets=()
    filter_horizontal=()
    list_filter=()

admin.site.register(Account,AccountAdmin)