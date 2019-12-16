from django.db import models


class Product(models.Model):
    name = models.CharField("name", max_length=50)
    desc = models.TextField("description", blank=True, null=True)
    price = models.FloatField("price")
    quantity = models.PositiveIntegerField("quantity", default=0)
    sold = models.PositiveIntegerField("sold", default=0)
    date_added = models.DateTimeField("date added", auto_now_add=True)
    category = models.ForeignKey("products.Category", models.CASCADE,
                                 related_name="products")
    sub_category = models.ForeignKey("products.SubCategory", models.CASCADE,
                                     related_name="products")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField("name", max_length=50)

    class Meta:
        ordering = ("name", )
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField("name", max_length=50)
    category = models.ForeignKey("products.Category", models.CASCADE,
                                 related_name="sub_categories")

    class Meta:
        ordering = ("name", )
        verbose_name_plural = "sub categories"

    def __str__(self):
        return self.name
