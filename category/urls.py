from django.urls import path
from .views import CategoryListView,ProductsListView,ItemListView,ItemCreateView,ItemDeleteView,ItemDetailView,ItemUpdateView

urlpatterns = [
    path('category/',CategoryListView.as_view(),name='category'),
    path('item/', ItemListView.as_view(), name='item_list'),
    path('item/new/', ItemCreateView.as_view(), name='item_create'),
    path('item/<int:pk>/edit/', ItemUpdateView.as_view(), name='item_update'),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
    path('product/', ProductsListView.as_view(), name='product'),
    path('product/ products_in_price_range/', ProductsListView.as_view(), name='products_in_price_range'),

]