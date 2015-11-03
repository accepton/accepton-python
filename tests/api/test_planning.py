import httpretty
import unittest
from datetime import datetime
from accepton import Client
from accepton.error import BadRequest
from accepton.plan import Plan
from tests import fixture_response


class SuccessfulPlanCreationTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.params = {
            "amount": 1000,
            "currency": "usd",
            "name": "Test Plan",
            "period_unit": "month"
        }
        url = "https://checkout.accepton.com/v1/recurring/plans"
        httpretty.enable()
        httpretty.register_uri(httpretty.POST,
                               url,
                               body=fixture_response("plan.json"),
                               status=201,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_makes_a_request(self):
        self.client.create_plan(**self.params)
        self.assertEqual(httpretty.has_request(), True)

    def test_returns_a_plan(self):
        plan = self.client.create_plan(**self.params)
        self.assertEqual(isinstance(plan, Plan), True)

    def test_plan_initialized_correctly(self):
        plan = self.client.create_plan(**self.params)
        self.assertEqual(plan.amount, 1000)
        self.assertEqual(isinstance(plan.created_at, datetime), True)
        self.assertEqual(plan.name, "Test Plan")
        self.assertEqual(plan.currency, "usd")
        self.assertEqual(plan.period_unit, "month")


class UnsuccessfulPlanCreationTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.params = {
            "amount": 1000,
            "currency": "usd",
            "name": "Test Plan",
            "period_unit": "month"
        }
        url = "https://checkout.accepton.com/v1/recurring/plans"
        httpretty.enable()
        httpretty.register_uri(httpretty.POST,
                               url,
                               body=fixture_response("invalid_name.json"),
                               status=400,
                               content_type="application/json")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_raises_bad_request_error(self):
        self.assertRaises(BadRequest,
                          lambda: self.client.create_plan(**self.params))
