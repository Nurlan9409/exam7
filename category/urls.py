from django.urls import path
from .views import CategoryListView,ProductsListView

urlpatterns = [
    path('category/',CategoryListView.as_view(),name='category'),
    path('product/',ProductsListView.as_view(),name='product'),
]