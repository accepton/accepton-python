from datetime import datetime
from .base import Base

__all__ = ["Plan"]


class Plan(Base):
    def __init__(self, attrs={}):
        super(Plan, self).__init__(attrs)

        self.initialize_attr("amount", int)
        self.initialize_attr("created_at", datetime)
        self.initialize_attr("currency", str)
        self.initialize_attr("name", str)
        self.initialize_attr("id", str)
        self.initialize_attr("period_unit", str)
