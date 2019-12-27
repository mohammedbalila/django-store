from django.contrib.auth.models import User
from rest_framework import generics
from . import serializer, models, permissions as custom_permissions


class UserListView(generics.ListAPIView):
    permission_classes = (custom_permissions.permissions.IsAdminUser,)
    queryset = models.CustomUser.objects.all()
    serializer_class = serializer.UserSerializer


class UserDeatilView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (custom_permissions.permissions.IsAuthenticated,custom_permissions.permissions.IsAdminUser)
    queryset = models.CustomUser.objects.all()
    serializer_class = serializer.UserSerializer


class CartListView(generics.ListCreateAPIView):
    permission_classes = (custom_permissions.IsUserOrAdmin,)
    queryset = models.Cart.objects.all()
    serializer_class = serializer.CartSerializer


class CartDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = (custom_permissions.IsUserOrAdmin,)
    queryset = models.Cart.objects.all()
    serializer_class = serializer.CartSerializer


class CartItemCreateView(generics.CreateAPIView):
    permission_classes = (custom_permissions.IsUser,)
    queryset = models.CartItem.objects.all()
    serializer_class = serializer.CartItemSerializer


class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (custom_permissions.IsUser,)
    queryset = models.CartItem.objects.all()
    serializer_class = serializer.CartItemSerializer
