import httpretty
import unittest
from datetime import datetime
from accepton import Client
from accepton.charge import Charge
from accepton.error import BadRequest, NotFound
from accepton.promo_code import PromoCode
from accepton.transaction_token import TransactionToken
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


class SuccessfulPromoCodeQueryTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        url = "https://checkout.accepton.com/v1/promo_codes/20OFF"
        httpretty.enable()
        httpretty.register_uri(httpretty.GET,
                               body=fixture_response("promo_code.json"),
                               uri=url,
                               status=200,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_makes_a_request(self):
        self.client.promo_code("20OFF")
        self.assertEqual(httpretty.has_request(), True)

    def test_returns_a_promo_code(self):
        promo_code = self.client.promo_code("20OFF")
        self.assertEqual(isinstance(promo_code, PromoCode), True)

    def test_promo_code_initialized_correctly(self):
        promo_code = self.client.promo_code("20OFF")
        self.assertEqual(isinstance(promo_code.created_at, datetime), True)
        self.assertEqual(promo_code.name, "20OFF")
        self.assertEqual(promo_code.promo_type, "amount")
        self.assertEqual(promo_code.value, 2000)


class SuccessfulPromoCodeSearchTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.params = {}
        httpretty.enable()
        httpretty.register_uri(httpretty.GET,
                               "https://checkout.accepton.com/v1/promo_codes",
                               body=fixture_response("promo_codes_list.json"),
                               status=200,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_returns_the_list_of_promo_codes(self):
        promo_codes = self.client.promo_codes()
        self.assertEqual(len(promo_codes), 2)
        for promo_code in promo_codes:
            self.assertEqual(isinstance(promo_code, PromoCode), True)


class SuccessfulTokenQueryTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.token_id = "txn_b43a7e1e51410639979ab2047c156caa"
        url = "https://checkout.accepton.com/v1/tokens/%s" % self.token_id
        httpretty.enable()
        httpretty.register_uri(httpretty.GET,
                               url,
                               body=fixture_response("token.json"),
                               status=200,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_makes_a_request(self):
        self.client.token(self.token_id)
        self.assertEqual(httpretty.has_request(), True)

    def test_returns_a_token(self):
        charge = self.client.token(self.token_id)
        self.assertEqual(isinstance(charge, TransactionToken), True)

    def test_charge_initialized_correctly(self):
        charge = self.client.token(self.token_id)
        self.assertEqual(charge.id, "txn_b43a7e1e51410639979ab2047c156caa")
        self.assertEqual(charge.amount, 100)
        self.assertEqual(charge.description, "Test Description")


class UnsuccessfulTokenQueryTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.token_id = "txn_b43a7e1e51410639979ab2047c156caa"
        url = "https://checkout.accepton.com/v1/tokens/%s" % self.token_id
        httpretty.enable()
        httpretty.register_uri(httpretty.GET,
                               url,
                               body=fixture_response("invalid_token.json"),
                               status=404,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_raises_not_found_error(self):
        self.assertRaises(NotFound,
                          lambda: self.client.token(self.token_id))
