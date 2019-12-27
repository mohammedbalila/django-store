from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
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
        fields = ("id", "user", "created_at",
                  "is_purchased", "purchase_date", "items")


"""User """


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ("id", "username", "email", "phone",
                  "first_name", "last_name", "phone")

class UserRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone = serializers.CharField()
    class Meta:
        model = models.CustomUser
        fields = ['username', 'first_name',
                  'last_name', 'email', 'phone']

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'phone': self.validated_data.get('phone', ''),
        }

    def custom_signup(self, request, user):
        user.phone = self.validated_data.get('phone')
        user.save()