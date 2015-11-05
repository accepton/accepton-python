from datetime import datetime
from .base import Base
from .plan import Plan

__all__ = ["Subscription"]


class Subscription(Base):
    def __init__(self, attrs={}):
        super(Subscription, self).__init__(attrs)

        self.initialize_attr("active", bool)
        self.initialize_attr("email", str)
        self.initialize_attr("id", str)
        self.initialize_attr("last_billed_at", datetime)
        self.initialize_attr("plan", Plan)
