from .version import VERSION

__all__ = ["Client"]


class Client(object):
    def __init__(self, api_key=None, environment="production"):
        self.api_key = api_key
        self.environment = environment
        self.user_agent = "accepton-python/{0}".format(VERSION)

    def has_api_key(self):
        return self.api_key is not None
