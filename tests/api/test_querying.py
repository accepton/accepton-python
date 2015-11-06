import httpretty
import unittest
from datetime import datetime
from accepton import Client
from accepton.charge import Charge
from accepton.error import BadRequest, NotFound
from accepton.plan import Plan
from accepton.promo_code import PromoCode
from accepton.subscription import Subscription
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


class SuccessfulPlanQueryTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.plan_id = "pln_123"
        url = ("https://checkout.accepton.com/v1/recurring/plans/%s" %
               self.plan_id)
        httpretty.enable()
        httpretty.register_uri(httpretty.GET,
                               url,
                               body=fixture_response("plan.json"),
                               status=200,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_makes_a_request(self):
        self.client.plan(self.plan_id)
        self.assertEqual(httpretty.has_request(), True)

    def test_returns_a_plan(self):
        plan = self.client.plan(self.plan_id)
        self.assertEqual(isinstance(plan, Plan), True)

    def test_plan_initialized_correctly(self):
        plan = self.client.plan(self.plan_id)
        self.assertEqual(plan.amount, 1000)
        self.assertEqual(isinstance(plan.created_at, datetime), True)
        self.assertEqual(plan.name, "Test Plan")
        self.assertEqual(plan.currency, "usd")
        self.assertEqual(plan.period_unit, "month")


class UnsuccessfulPlanQueryTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.plan_id = "chg_123"
        url = ("https://checkout.accepton.com/v1/recurring/plans/%s" %
               self.plan_id)
        httpretty.enable()
        httpretty.register_uri(httpretty.GET,
                               url,
                               body=fixture_response("invalid_plan_id.json"),
                               status=400,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_raises_bad_request_error(self):
        self.assertRaises(BadRequest,
                          lambda: self.client.plan(self.plan_id))


class SuccessfulPlanSearchTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.params = {}
        url = "https://checkout.accepton.com/v1/recurring/plans"
        httpretty.enable()
        httpretty.register_uri(httpretty.GET,
                               url,
                               body=fixture_response("plans_list.json"),
                               status=200,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_returns_the_list_of_plans(self):
        plans = self.client.plans()
        self.assertEqual(len(plans), 3)
        for plan in plans:
            self.assertEqual(isinstance(plan, Plan), True)


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


class SuccessfulSubscriptionSearchTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.params = {"plan_token": "pln_965d6898b660d85b"}
        url = "https://checkout.accepton.com/v1/recurring/subscriptions"
        httpretty.enable()
        httpretty.register_uri(httpretty.GET,
                               url,
                               body=fixture_response("subscriptions.json"),
                               status=200,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_returns_the_list_of_subscriptions(self):
        subscriptions = self.client.subscriptions(**self.params)
        self.assertEqual(len(subscriptions), 1)
        for subscription in subscriptions:
            self.assertEqual(isinstance(subscription, Subscription), True)

    def test_plan_token_converted_successfully(self):
        self.client.subscriptions(**self.params)
        self.assertEqual(httpretty.last_request().querystring,
                         {"plan.token": ["pln_965d6898b660d85b"]})


class SuccessfulSubscriptionQueryTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.subscription_id = "sub_123"
        url = ("https://checkout.accepton.com/v1/recurring/subscriptions/%s" %
               self.subscription_id)
        httpretty.enable()
        httpretty.register_uri(httpretty.GET,
                               url,
                               body=fixture_response("subscription.json"),
                               status=200,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_makes_a_request(self):
        self.client.subscription(self.subscription_id)
        self.assertEqual(httpretty.has_request(), True)

    def test_returns_a_subscription(self):
        subscription = self.client.subscription(self.subscription_id)
        self.assertEqual(isinstance(subscription, Subscription), True)

    def test_subscription_initialized_correctly(self):
        sub = self.client.subscription(self.subscription_id)
        self.assertEqual(sub.active, False)
        self.assertEqual(sub.email, "test1@email.com")
        self.assertEqual(sub.id, "sub_123")
        self.assertEqual(isinstance(sub.last_billed_at, datetime), True)
        self.assertEqual(isinstance(sub.plan, Plan), True)
        self.assertEqual(sub.plan.id, "pln_965d6898b660d85b")


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
