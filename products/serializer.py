from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(read_only=True)
    sub_categories = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = models.Category
        fields = "__all__"

class SubCategorySerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = models.SubCategory
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"