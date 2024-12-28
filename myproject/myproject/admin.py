from django.contrib import admin
from myproject.models import User , Product



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'name', 'email']
    list_display = ['username', 'name', 'email']
    search_fields = ['username', 'name', 'email']
    
@admin.register(Product)
class UserAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'stock']
    list_display =  ['name', 'price', 'stock']
    search_fields = ['name', 'price', 'stock']
    
# admin.site.register(User)
# admin.site.register(Product)
