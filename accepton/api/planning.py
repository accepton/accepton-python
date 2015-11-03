from ..plan import Plan
from .utils import Utils


class Planning(Utils):
    def create_plan(self, amount=None, name=None, currency=None,
                    period_unit=None):
        """Create a plan on AcceptOn

        :param amount: The amount in cents of the plan.
        :type amount: int.
        :param name: The name of the plan.
        :type name: str.
        :param currency: The currency to charge in (default: usd).
        :type currency: str.
        :param period_unit: The unit of billing frequency.
        :type period_unit: str.

        :returns: Plan -- The created Plan.
        :raises: accepton.Error

        :Example:

        # Create a plan named "Test Plan"
        >> client.create_plan(amount=2000, currency="usd",
                              name="Test Plan", period_unit="month")
        """
        return self.perform_post_with_object("/v1/recurring/plans",
                                             self.as_params(locals()),
                                             Plan)
