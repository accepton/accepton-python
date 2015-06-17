import httpretty
import unittest
from accepton.client import Client
from accepton.request import Request
from accepton.response import Response


class RequestTest(unittest.TestCase):

    def setUp(self):
        self.client = Client(api_key="skey_123")
        self.request = Request(self.client, "get", "/path")
        httpretty.enable()
        httpretty.register_uri(httpretty.GET,
                               "https://checkout.accepton.com/path",
                               body='{"foo":"bar"}')

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_bearer_authorization_header(self):
        self.request.perform()
        self.assertEqual(httpretty.last_request().headers["authorization"],
                         "Bearer skey_123")

    def test_perform_makes_a_request(self):
        self.request.perform()
        self.assertEqual(httpretty.has_request(), True)

    def test_perform_returns_a_response(self):
        response = self.request.perform()
        self.assertEqual(isinstance(response, Response), True)
        self.assertEqual(response.foo, 'bar')

    def test_user_agent_set_from_client(self):
        self.request.perform()
        self.assertEqual(httpretty.last_request().headers["user-agent"],
                         self.client.user_agent)
