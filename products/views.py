from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from . import serializer, models, permissions as custom_permissions


class ProductListView(generics.ListCreateAPIView):
    permission_classes = [
        custom_permissions.permissions.IsAuthenticatedOrReadOnly, ]
    queryset = models.Product.objects.all().order_by("-sold")
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


class ReviewList(generics.ListCreateAPIView):
    pagination_class = None
    serializer_class = serializer.ReviewSerializer

    def get_queryset(self):
        queryset = models.Review.objects.filter(
            product=self.kwargs['product_pk'])
        return queryset


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializer.ReviewSerializer


class DiscountList(generics.ListCreateAPIView):
    serializer_class = serializer.DiscountSerializer
    queryset = models.Discount.objects.all()


class DiscountDetailView(generics.ListAPIView):
    # queryset = models.Discount.objects.all()
    serializer_class = serializer.ProductSerializer
    lookup_field = "discount_id"

    def get_queryset(self):
        queryset = models.Product.objects.filter(
            discount=self.kwargs["discount_id"])
        return queryset
