import httpretty
import unittest
from datetime import datetime
from accepton import Client
from accepton.error import Unauthorized
from accepton.plan import Plan
from accepton.subscription import Subscription
from tests import fixture_response


class SuccessfulSubscriptionCancellationTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.sub_id = "sub_123"
        url = ("https://checkout.accepton.com/v1/subscriptions/%s/cancel" %
               self.sub_id)
        httpretty.enable()
        httpretty.register_uri(httpretty.POST,
                               url,
                               body=fixture_response("subscription.json"),
                               status=200,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_makes_a_request(self):
        self.client.cancel_subscription(self.sub_id)
        self.assertEqual(httpretty.has_request(), True)

    def test_returns_a_subscription(self):
        subscription = self.client.cancel_subscription(self.sub_id)
        self.assertEqual(isinstance(subscription, Subscription), True)

    def test_subscription_initialized_correctly(self):
        sub = self.client.cancel_subscription(self.sub_id)
        self.assertEqual(sub.active, False)
        self.assertEqual(sub.email, "test1@email.com")
        self.assertEqual(sub.id, "sub_123")
        self.assertEqual(isinstance(sub.last_billed_at, datetime), True)
        self.assertEqual(isinstance(sub.plan, Plan), True)


class UnsuccessfulSubscriptionCancellationTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.sub_id = "sub_123"
        url = ("https://checkout.accepton.com/v1/subscriptions/%s/cancel" %
               self.sub_id)
        httpretty.enable()
        httpretty.register_uri(httpretty.POST,
                               url,
                               body=fixture_response("cancel_failure.json"),
                               status=401,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_raises_unauthorized_error(self):
        self.assertRaises(Unauthorized,
                          lambda: self.client.cancel_subscription(self.sub_id))
