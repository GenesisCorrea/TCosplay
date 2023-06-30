from django.contrib import admin
from .models import Producto,contacto


class ProductoAdmin(admin.ModelAdmin):
    list_display  =  ["codigo","nombre","precio"]   
    list_editable =  ["precio"]                     
    search_fields =  ["nombre"]                     
    list_filter   =  ["precio"]                     



admin.site.register(Producto,ProductoAdmin)
admin.site.register(contacto)
