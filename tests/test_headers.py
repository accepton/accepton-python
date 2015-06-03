import unittest
import accepton
from accepton.headers import Headers


class HeadersTest(unittest.TestCase):

    def setUp(self):
        self.client = accepton.Client(api_key="skey_123")
        self.headers = Headers(self.client)
        self.request_headers = self.headers.request_headers()

    def test_accept_header(self):
        self.assertEqual("application/json", self.request_headers["accept"])

    def test_bearer_token(self):
        self.assertEqual("Bearer skey_123",
                         self.request_headers["authorization"])

    def test_user_agent(self):
        self.assertEqual(self.client.user_agent,
                         self.request_headers["user-agent"])
