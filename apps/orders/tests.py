from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from apps.products.models import Category, Product, Seller
from .models import Order


class OrderStockValidationTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(phone='1234567890', password='testpass')
        self.category = Category.objects.create(name='Test')
        self.seller = Seller.objects.create(name='Test seller')
        self.product = Product.objects.create(
            name='Test product',
            description='A product for tests',
            price=10.00,
            category=self.category,
            seller=self.seller,
            stock=100,
            is_active=True,
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_order_fails_when_quantity_exceeds_stock(self):
        payload = {
            'recipient_name': 'John Doe',
            'recipient_phone': '0123456789',
            'courier_note': '',
            'address': '123 Test St',
            'items': [
                {'product': self.product.id, 'quantity': 150},
            ],
        }

        response = self.client.post('/api/v1/orders/', payload, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Insufficient stock', str(response.data))

    def test_order_succeeds_when_quantity_is_within_stock(self):
        payload = {
            'recipient_name': 'John Doe',
            'recipient_phone': '0123456789',
            'courier_note': '',
            'address': '123 Test St',
            'items': [
                {'product': self.product.id, 'quantity': 50},
            ],
        }

        response = self.client.post('/api/v1/orders/', payload, format='json')
        self.assertEqual(response.status_code, 201)
        
        # Stock should NOT be decremented on order creation (only when paid)
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 100)
        
        # Now change order status to paid and check stock is decremented
        # Get the created order (should be the only one for this user)
        order_obj = Order.objects.filter(user=self.user).first()
        self.assertIsNotNone(order_obj)
        order_obj.status = 'paid'
        order_obj.save()
        
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 50)
