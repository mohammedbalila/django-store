from django.contrib.auth.models import User
from rest_framework import serializers
from . import models

""" Cart item """
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartItem
        fields = ("id", "cart", "product" "quantity", "price")

""" Cart """
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = models.Cart
        fields = ("id", "user", "create_at", "is_purchased", "purchase_date")

"""User """
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")
