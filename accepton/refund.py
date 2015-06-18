from datetime import datetime
from .base import Base

__all__ = ['Refund']


class Refund(Base):
    def __init__(self, attrs={}):
        super(Refund, self).__init__(attrs)

        self.initialize_attr("amount", int)
        self.initialize_attr("created", datetime)
        self.initialize_attr("currency", str)
        self.initialize_attr("id", str)
        self.initialize_attr("metadata", dict)
        self.initialize_attr("reason", str)
