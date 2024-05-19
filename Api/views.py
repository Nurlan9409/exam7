from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from category.models import Category,Product,Review
from users.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import CategorySerializer, ProductsSerializer, UserSerializer,ReviewSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets


class CategoryListAPIViewSet(ModelViewSet):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
        permission_classes = [IsAuthenticated]
        authentication_classes = [TokenAuthentication]
        filter_backends = (filters.SearchFilter,)
        search_fields = ('price','product__price',)
class ProductlAPIViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title','category__title')


class UsersListAPIViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name')

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(product=self.request.user)




