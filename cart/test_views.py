from django.test import TestCase
from products.models import Category, Product
from decimal import Decimal
# Create your tests here.
class TestCartViews(TestCase):
    
    def test_view_cart(self):
        page = self.client.get("/cart/view/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart/view_cart.html")
        
        
    def test_get_404_on_add_to_cart_with_no_product_id(self):
        response = self.client.get("cart/add/")
        self.assertEqual(response.status_code, 404)