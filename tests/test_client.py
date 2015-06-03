import unittest
import accepton


class ClientTest(unittest.TestCase):

    def test_configurable_environment(self):
        client = accepton.Client(environment="development")
        self.assertEqual("development", client.environment)

    def test_defaults_to_production_environment(self):
        client = accepton.Client()
        self.assertEqual("production", client.environment)

    def test_has_api_key_is_true_when_configured(self):
        client = accepton.Client(api_key="abc123")
        self.assertEqual(True, client.has_api_key())

    def test_has_api_key_is_false_when_not_configured(self):
        client = accepton.Client()
        self.assertEqual(False, client.has_api_key())

    def test_user_agent(self):
        expected = "accepton-python/{0}".format(accepton.__version__)
        actual = accepton.Client().user_agent
        self.assertEqual(expected, actual)
