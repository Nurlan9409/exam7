from django.contrib import admin
from .models import Category,Product
from import_export.admin import ImportExportModelAdmin



@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['id','title','create_date']
    list_display_link = ['id','title','create_date']
    search_fields =  ['id','title','price','description']


@admin.register(Product)
class ProductsAdmin(ImportExportModelAdmin):
    list_display = ['id','title','price','description']
    list_display_link = ['id','title','price','description']
    search_field= ['id','title','price','description']

from django.contrib import admin

# Register your models here.
