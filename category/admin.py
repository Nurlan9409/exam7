from django.contrib import admin
from .models import Category,Product
from import_export.admin import ImportExportModelAdmin



@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['id','title','create_date']
    list_display_link = ['id','title','create_date']
    search_fields =  ['id','title',]
    ordering = ['title',]


@admin.register(Product)
class ProductsAdmin(ImportExportModelAdmin):
    list_display = ['id','title','price','description']
    list_display_link = ['id','title','price','description']
    search_fields = ['id','title','price',]
    ordering = ['title','price',]

