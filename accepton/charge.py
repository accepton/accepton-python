from datetime import datetime
from .base import Base

__all__ = ['Charge']


class Charge(Base):
    def __init__(self, attrs={}):
        super(Charge, self).__init__(attrs)

        self.initialize_attr("amount", int)
        self.initialize_attr("application_fee", int)
        self.initialize_attr("created_at", datetime)
        self.initialize_attr("currency", str)
        self.initialize_attr("description", str)
        self.initialize_attr("id", str)
        self.initialize_attr("metadata", dict)
        self.initialize_attr("refunded", bool)
        self.initialize_attr("remote_id", str)
        self.initialize_attr("status", str)
