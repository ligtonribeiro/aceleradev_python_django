from django.test import TestCase
from .models import Products

class ProductStrTestCase(TestCase):
    def test_str_should_return_name(self):
        product = Products.objects.create(
            name = 'Teste Produto',
            description = 'Teste Descrição',
            price = 10.5
        )
    
        self.assertEqual(str(product), 'Teste Produto')
