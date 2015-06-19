import httpretty
import unittest
from datetime import datetime
from accepton import Client
from accepton.error import BadRequest
from accepton.refund import Refund
from tests import fixture_response


class SuccessfulRefundTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.params = {"amount": 100, "charge_id": "chg_123"}
        httpretty.enable()
        httpretty.register_uri(httpretty.POST,
                               "https://checkout.accepton.com/v1/refunds",
                               body=fixture_response("refund.json"),
                               status=201,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_makes_a_request(self):
        self.client.refund(**self.params)
        self.assertEqual(httpretty.has_request(), True)

    def test_returns_a_refund(self):
        refund = self.client.refund(**self.params)
        self.assertEqual(isinstance(refund, Refund), True)

    def test_transaction_refund_initialized_correctly(self):
        refund = self.client.refund(**self.params)
        self.assertEqual(refund.id, "ref_123")
        self.assertEqual(refund.amount, 100)
        self.assertEqual(isinstance(refund.created, datetime), True)
        self.assertEqual(refund.currency, "usd")
        self.assertEqual(refund.metadata, {})
        self.assertEqual(refund.reason, "requested_by_customer")


class UnsuccessfulRefundTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.params = {}
        httpretty.enable()
        httpretty.register_uri(httpretty.POST,
                               "https://checkout.accepton.com/v1/refunds",
                               body=fixture_response("invalid_amount.json"),
                               status=400,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_raises_bad_request_error(self):
        self.assertRaises(BadRequest,
                          lambda: self.client.refund(**self.params))
