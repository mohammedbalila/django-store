from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from . import models


class ProductModelTest(TestCase):
    client = APIClient()
    @classmethod
    def setUpTestData(cls):
        url = reverse('product-list')
        category = models.Category.objects.create(name='Men')
        sub_category = models.SubCategory.objects.create(
            name='Shirts', category=category)
        product = models.Product.objects.create(
            name='Air Jordan', price=100.0, quantity=10,
            sold=5, category=category, sub_category=sub_category,
            desc='Nice shoes to have'
        )

    def test_product_list(self):
        url = reverse('product-list')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_product_create(self):
        url = reverse('product-list')
        data = {
            'name': 'One', 'price': 50.0,
            'quantity': 5, 'sold': 1,
            'category': 1, 'sub_category': 1,
            'desc': 'May be used to represent the target of One'
        }
        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Product.objects.count(), 2)

    def test_product_detail(self):
        url = reverse('product-detail', kwargs={'pk': 1})
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data.get('name'), 'Air Jordan')

    def test_product_delete(self):
        url = reverse('product-detail', kwargs={'pk': 1})
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.Product.objects.count(), 0)

    def test_product_update(self):
        # !!TODO
        pass
