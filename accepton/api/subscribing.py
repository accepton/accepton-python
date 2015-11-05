from ..subscription import Subscription
from .utils import Utils


class Subscribing(Utils):
    def cancel_subscription(self, id):
        url = "/v1/subscriptions/%s/cancel" % id
        return self.perform_post_with_object(url, {}, Subscription)
