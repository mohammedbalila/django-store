from django.contrib import admin
from . import models

admin.site.register([
    models.Category,
    models.SubCategory,
    models.Product
])
