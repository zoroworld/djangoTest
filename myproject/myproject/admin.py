from django.contrib import admin
from myproject.models.User import User
from myproject.models.Product import Product


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['title', 'username', 'name', 'email']
    list_display = ['id','username', 'name', 'email']
    search_fields = ['username', 'name', 'email']
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # fields = ['seller', 'name', 'price', 'stock']
    list_display =  ['id', 'name', 'price', 'stock']
    search_fields = ['name', 'price', 'stock']
    save_as = True
    fieldsets = (
        ("Product Info", {
            'fields':('seller', 'name')
        }),
        ("Stock Info", {
            'fields':('price', 'stock'),
            'classes':('collapse', 'open'),
        })
    )
    
# admin.site.register(User)
# admin.site.register(Product)