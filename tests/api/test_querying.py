import httpretty
import unittest
from datetime import datetime
from accepton import Client
from accepton.charge import Charge
from accepton.error import BadRequest
from tests import fixture_response


class SuccessfulChargeSearchTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.params = {}
        httpretty.enable()
        httpretty.register_uri(httpretty.GET,
                               "https://checkout.accepton.com/v1/charges",
                               body=fixture_response("charges_list.json"),
                               status=200,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_returns_the_list_of_charges(self):
        charges = self.client.charges()
        self.assertEqual(len(charges), 3)
        for charge in charges:
            self.assertEqual(isinstance(charge, Charge), True)


class SuccessfulChargeQueryTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.charge_id = "chg_ff6024ab78980de7"
        url = "https://checkout.accepton.com/v1/charges/%s" % self.charge_id
        httpretty.enable()
        httpretty.register_uri(httpretty.GET,
                               url,
                               body=fixture_response("charge.json"),
                               status=200,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_makes_a_request(self):
        self.client.charge(self.charge_id)
        self.assertEqual(httpretty.has_request(), True)

    def test_returns_a_charge(self):
        charge = self.client.charge(self.charge_id)
        self.assertEqual(isinstance(charge, Charge), True)

    def test_charge_initialized_correctly(self):
        charge = self.client.charge(self.charge_id)
        self.assertEqual(charge.id, "chg_ff6024ab78980de7")
        self.assertEqual(charge.amount, 1000)
        self.assertEqual(charge.application_fee, None)
        self.assertEqual(isinstance(charge.created_at, datetime), True)
        self.assertEqual(charge.currency, 'usd')
        self.assertEqual(charge.description, "Test Transaction")
        self.assertEqual(charge.metadata, {})
        self.assertEqual(charge.refunded, False)
        self.assertEqual(charge.remote_id, "ch_16I54f2EZMTOjTLjGB8nd84P")
        self.assertEqual(charge.status, 'paid')


class UnsuccessfulChargeQueryTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.charge_id = "chg_123"
        url = "https://checkout.accepton.com/v1/charges/%s" % self.charge_id
        httpretty.enable()
        httpretty.register_uri(httpretty.GET,
                               url,
                               body=fixture_response("invalid_charge_id.json"),
                               status=400,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_raises_bad_request_error(self):
        self.assertRaises(BadRequest,
                          lambda: self.client.charge(self.charge_id))
