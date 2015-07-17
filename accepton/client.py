from .api.promotion import Promotion
from .api.querying import Querying
from .api.refunding import Refunding
from .api.tokenization import Tokenization
from .version import VERSION

__all__ = ["Client"]


class Client(Promotion, Querying, Refunding, Tokenization):
    def __init__(self, api_key=None, environment="production"):
        self.api_key = api_key
        self.environment = environment
        self.user_agent = "accepton-python/{0}".format(VERSION)

    def has_api_key(self):
        return self.api_key is not None
