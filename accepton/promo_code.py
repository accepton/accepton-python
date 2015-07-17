from datetime import datetime
from .base import Base

__all__ = ["PromoCode"]


class PromoCode(Base):
    def __init__(self, attrs={}):
        super(PromoCode, self).__init__(attrs)

        self.initialize_attr("created_at", datetime)
        self.initialize_attr("name", str)
        self.initialize_attr("promo_type", str)
        self.initialize_attr("value", float)
        self.original_name = self.name

    def as_params(self):
        return {"name": self.name,
                "promo_type": self.promo_type,
                "value": self.value}
