import unittest
import requests


class TestProduct(unittest.TestCase):

    def test_get_products(self):
        response = requests.get('http://localhost:5000/products')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)
