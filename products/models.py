from django.db import models


class Product(models.Model):
    name = models.CharField("name", max_length=50)
    desc = models.TextField("description", blank=True, null=True)
    price = models.FloatField("price")
    quantity = models.PositiveIntegerField("quantity", default=0)
    sold = models.PositiveIntegerField("sold", default=0)
    image = models.ImageField(upload_to='products/', blank=True)
    date_added = models.DateTimeField("date added", auto_now_add=True)
    category = models.ForeignKey("products.Category", models.CASCADE,
                                 related_name="products")
    sub_category = models.ForeignKey("products.SubCategory", models.CASCADE,
                                     related_name="products")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField("name", max_length=50)
    image = models.ImageField(upload_to="categories/")

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


class Review(models.Model):
    user = models.ForeignKey(
        "accounts.CustomUser", related_name="reviews", on_delete=models.CASCADE)
    comment = models.TextField()
    rateing = models.FloatField()
    up_votes = models.IntegerField(
        verbose_name="upVotes", default=0, blank=True)
    down_votes = models.IntegerField(
        verbose_name="downVotes", default=0, blank=True)
    product = models.ForeignKey(
        "products.Product", related_name="reviews", on_delete=models.CASCADE)
