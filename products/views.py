from rest_framework import generics
from . import serializer, models

class ProductListView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializer.CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializer.CategorySerializer

class SubCategoryList(generics.ListCreateAPIView):
    queryset = models.SubCategory.objects.all()
    serializer_class = serializer.SubCategorySerializer

class SubCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SubCategory.objects.all()
    serializer_class = serializer.SubCategorySerializer