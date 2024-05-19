from django.shortcuts import render, redirect
from django.views import View
from .models import Product,Category,Search
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db.models import Q

from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .forms import CategoryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class CategoryListView(View):
    def get(self,request):
        category = Category.objects.all()
        contex = {
            'category':category,
        }
        return render(request, 'main/shop.html',contex)

    @action(detail=True, methods=['GET'])
    def look(self, request, *args, **kwargs):
        category = self.get_object()
        category.watched += 1
        category.save()
        return Response(category.watched, status=status.HTTP_200_OK)




class ProductsListView(View):
    def get(self,request):
        product= Product.objects.all()
        contex = {
            'product':product
        }
        return render(request, 'main/shop.html',contex)

    @action(detail=True, methods=['GET'])
    def buy_counter(self,request,*args,**kwargs):
        product = self.get_object()
        product.buy_count+= 1
        product.save()
        return (Response(product.buy_count,status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET']))
    def reyting(self,request,*args,**kwargs):
        product = self.get_object()
        product.reyting+= 1
        product.save()
        return Response(product.reyting,status=status.HTTP_200_OK)


    @action(detail=True, methods=['GET'])
    def remaining(self,request,*args,**kwargs):
        product = self.get_object()
        product.remaining-= 1
        product.save()
        return Response(product.buy_count,status=status.HTTP_200_OK)

class SearchResultsView(View):
    def get(self, request):
        query = request.GET.get('query')
        results = Product.objects.filter(title=query)
        return render(request, 'search_results.html', {'results': results, 'query': query})




class ItemListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'main/item_list.html'
    context_object_name = 'items'

class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'main/item_detail.html'
    context_object_name = 'item'

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'main/item_form.html'
    success_url = reverse_lazy('item_list')

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'main/item_form.html'
    success_url = reverse_lazy('item_list')

class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'main/item_confirm_delete.html'
    success_url = reverse_lazy('item_list')