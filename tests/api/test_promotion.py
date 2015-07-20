import httpretty
import unittest
from datetime import datetime
from accepton import Client
from accepton.error import BadRequest
from accepton.promo_code import PromoCode
from tests import fixture_response


class SuccessfulPromoCodeCreationTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.params = {"name": "20OFF", "promo_type": "amount", "value": 2000}
        httpretty.enable()
        httpretty.register_uri(httpretty.POST,
                               "https://checkout.accepton.com/v1/promo_codes",
                               body=fixture_response("promo_code.json"),
                               status=201,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_makes_a_request(self):
        self.client.create_promo_code(**self.params)
        self.assertEqual(httpretty.has_request(), True)

    def test_returns_a_promo_code(self):
        promo_code = self.client.create_promo_code(**self.params)
        self.assertEqual(isinstance(promo_code, PromoCode), True)

    def test_promo_code_initialized_correctly(self):
        promo_code = self.client.create_promo_code(**self.params)
        self.assertEqual(isinstance(promo_code.created_at, datetime), True)
        self.assertEqual(promo_code.name, "20OFF")
        self.assertEqual(promo_code.promo_type, "amount")
        self.assertEqual(promo_code.value, 2000)


class UnsuccessfulPromoCodeCreationTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.params = {"name": "", "promo_type": "amount", "value": 2000}
        httpretty.enable()
        httpretty.register_uri(httpretty.POST,
                               "https://checkout.accepton.com/v1/promo_codes",
                               body=fixture_response("invalid_name.json"),
                               status=400,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_raises_bad_request_error(self):
        self.assertRaises(BadRequest,
                          lambda: self.client.create_promo_code(**self.params))


class SuccessfulPromoCodeDeletionTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.promo_code = PromoCode({"name": "20OFF",
                                     "promo_type": "amount",
                                     "value": 2000})
        url = "https://checkout.accepton.com/v1/promo_codes/20OFF"
        httpretty.enable()
        httpretty.register_uri(httpretty.DELETE,
                               body=fixture_response("promo_code.json"),
                               uri=url,
                               status=200,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_makes_a_request(self):
        self.client.delete_promo_code(self.promo_code)
        self.assertEqual(httpretty.has_request(), True)

    def test_returns_a_promo_code(self):
        promo_code = self.client.delete_promo_code(self.promo_code)
        self.assertEqual(isinstance(promo_code, PromoCode), True)

    def test_promo_code_initialized_correctly(self):
        promo_code = self.client.delete_promo_code(self.promo_code)
        self.assertEqual(isinstance(promo_code.created_at, datetime), True)
        self.assertEqual(promo_code.name, "20OFF")
        self.assertEqual(promo_code.promo_type, "amount")
        self.assertEqual(promo_code.value, 2000)


class SuccessfulPromoCodeUpdateTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.promo_code = PromoCode({"name": "10OFF",
                                     "promo_type": "amount",
                                     "value": 1000})
        url = "https://checkout.accepton.com/v1/promo_codes/10OFF"
        httpretty.enable()
        httpretty.register_uri(httpretty.PUT,
                               body=fixture_response("promo_code.json"),
                               uri=url,
                               status=200,
                               content_type="application/json")

        self.promo_code.name = '20OFF'
        self.promo_code.value = 2000

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_makes_a_request(self):
        self.client.update_promo_code(self.promo_code)
        self.assertEqual(httpretty.has_request(), True)

    def test_returns_a_promo_code(self):
        promo_code = self.client.update_promo_code(self.promo_code)
        self.assertEqual(isinstance(promo_code, PromoCode), True)

    def test_promo_code_initialized_correctly(self):
        promo_code = self.client.update_promo_code(self.promo_code)
        self.assertEqual(isinstance(promo_code.created_at, datetime), True)
        self.assertEqual(promo_code.name, "20OFF")
        self.assertEqual(promo_code.promo_type, "amount")
        self.assertEqual(promo_code.value, 2000)
