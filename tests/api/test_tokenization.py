import httpretty
import unittest
from datetime import datetime
from accepton import Client
from accepton.error import BadRequest
from accepton.transaction_token import TransactionToken
from tests import fixture_response


class SuccessfulTokenizationTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.params = {"amount": 100, "description": "Test Description"}
        httpretty.enable()
        httpretty.register_uri(httpretty.POST,
                               "https://checkout.accepton.com/v1/tokens",
                               body=fixture_response("token.json"),
                               status=201,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_makes_a_request(self):
        self.client.create_token(**self.params)
        self.assertEqual(httpretty.has_request(), True)

    def test_returns_a_transaction_token(self):
        token = self.client.create_token(**self.params)
        self.assertEqual(isinstance(token, TransactionToken), True)

    def test_transaction_token_initialized_correctly(self):
        token = self.client.create_token(**self.params)
        self.assertEqual(token.id, "txn_b43a7e1e51410639979ab2047c156caa")
        self.assertEqual(token.amount, 100)
        self.assertEqual(isinstance(token.created, datetime), True)
        self.assertEqual(token.description, "Test Description")


class UnsuccessfulTokenizationTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.params = {}
        httpretty.enable()
        httpretty.register_uri(httpretty.POST,
                               "https://checkout.accepton.com/v1/tokens",
                               body=fixture_response("invalid_amount.json"),
                               status=400,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_raises_bad_request_error(self):
        self.assertRaises(BadRequest,
                          lambda: self.client.create_token(**self.params))
