from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from . import serializer, models, permissions as custom_permissions


class ProductListView(generics.ListCreateAPIView):
    permission_classes = [
        custom_permissions.permissions.IsAuthenticatedOrReadOnly, ]
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'sub_category']


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (custom_permissions.IsUserOrAdminOrReadOnly, )
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer


class CategoryList(generics.ListCreateAPIView):
    pagination_class = None
    queryset = models.Category.objects.all()
    serializer_class = serializer.CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (custom_permissions.IsUserOrAdminOrReadOnly, )
    queryset = models.Category.objects.all()
    serializer_class = serializer.CategorySerializer


class SubCategoryList(generics.ListCreateAPIView):
    pagination_class = None
    queryset = models.SubCategory.objects.all()
    serializer_class = serializer.SubCategorySerializer


class SubCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (custom_permissions.IsAdmin,)
    queryset = models.SubCategory.objects.all()
    serializer_class = serializer.SubCategorySerializer
