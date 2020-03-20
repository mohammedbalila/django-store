from django.db.models import Avg
from django.contrib.auth.models import User
from rest_framework import serializers
from . import models
from accounts.models import CustomUser


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


class ReviewSerializer(serializers.ModelSerializer):
    user_info = serializers.SerializerMethodField()

    def get_user_info(self, obj):
        user = CustomUser.objects.get(pk=obj.user.id)
        return {"id": user.id, "username": user.username, "email": user.email}

    class Meta:
        model = models.Review
        fields = ("id", "user", "product", "user_info", "comment",
                  "rating", "up_votes", "down_votes")


class ProductSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()

    def get_reviews(self, obj):
        reviews = models.Review.objects.filter(product=obj.id)
        review = reviews.aggregate(Avg("rating"))
        return {"count": len(reviews), "rating": review["rating__avg"]}

    class Meta:
        model = models.Product
        fields = "__all__"
