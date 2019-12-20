from django.db import models
from django.conf import settings


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="carts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    is_purchased = models.BooleanField(default=False)
    purchase_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["created_at"]


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, models.CASCADE,
                             related_name="items")
    product = models.ForeignKey(
        "products.Product", models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.product.name
