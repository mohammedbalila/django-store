from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

""" Cart item """
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartItem
        fields = ("id", "cart", "product" "quantity", "price")

""" Cart """
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = models.Cart
        fields = ("id", "user", "created_at", "is_purchased", "purchase_date", 'items')

"""User """
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ("id", "username", "email", 'phone')
