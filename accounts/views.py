from django.contrib.auth.models import User
from rest_framework import generics
from . import serializer, models


class UserListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializer.UserSerializer


class UserDeatilView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializer.UserSerializer


class CartListView(generics.ListCreateAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = serializer.CartSerializer


class CartDetailView(generics.RetrieveUpdateAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = serializer.CartSerializer


class CartItemCreateView(generics.CreateAPIView):
    queryset = models.CartItem.objects.all()
    serializer_class = serializer.CartItemSerializer


class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CartItem.objects.all()
    serializer_class = serializer.CartItemSerializer
