from datetime import datetime
from .base import Base

__all__ = ['TransactionToken']


class TransactionToken(Base):
    def __init__(self, attrs={}):
        super(TransactionToken, self).__init__(attrs)

        self.initialize_attr("amount", int)
        self.initialize_attr("application_fee", int)
        self.initialize_attr("created", datetime)
        self.initialize_attr("description", str)
        self.initialize_attr("id", str)
        self.initialize_attr("merchant_paypal_account", str)
