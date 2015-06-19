from ..refund import Refund
from .utils import Utils


class Refunding(Utils):
    """Refund a charge by the specified amount.

    :param amount: The amount in cents to refund.
    :type amount: int.
    :param charge_id: The id of the charge to refund.
    :type charge_id: str

    :returns: Refund -- The created Refund.
    :raises: accepton.Error

    :Example:

    # Create a refund of $1.00 on charge chg_47ce6dacb1ec5124
    >> client.refund(amount=100, charge_id="chg_47ce6dacb1ec5124")
    """
    def refund(self, amount=None, charge_id=None):
        return self.perform_post_with_object("/v1/refunds",
                                             self.as_params(locals()),
                                             Refund)
