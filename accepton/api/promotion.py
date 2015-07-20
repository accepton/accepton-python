from ..promo_code import PromoCode
from .utils import Utils


class Promotion(Utils):
    def create_promo_code(self, name=None, promo_type=None, value=None):
        """Create a promo code on AcceptOn

        :param name: The promo code name, as given to customers.
        :type name: str.
        :param promo_type: The type of promo code.
        :type promo_type: str.
        :param value: The promo code amount.
        :type value: int, float.

        :returns: PromoCode -- The created promo code.
        :raises: accepton.Error

        :Example:

        # Create a "20OFF" promo code for $20 off of a purchase.
        >> client.create_promo_code(name="20OFF", promo_type="amount",
                                    value=2000)

        # Create a "10-percent" promo code for 10% off of a purchase.
        >> client.create_promo_code(name="10-percent", promo_type="percentage",
                                    value=10.0)

        # Create a "5dollar" promo code that reduces a purchase to $5.00.
        >> client.create_promo_code(name="5dollar", promo_type="fixed_price",
                                    value=500)

        """
        return self.perform_post_with_object("/v1/promo_codes",
                                             self.as_params(locals()),
                                             PromoCode)

    def delete_promo_code(self, promo_code):
        """Delete a promo code on AcceptOn

        :param promo_code: The promo code to delete.
        :type promo_code: PromoCode.

        :returns: PromoCode -- The deleted promo code.
        :raises: accepton.Error

        :Example:

        # Delete a promo code previously retrieved by the client
        >> client.delete_promo_code(promo_code)
        """
        return self.perform_delete_with_object(
            "/v1/promo_codes/%s" % promo_code.original_name,
            {},
            PromoCode)

    def update_promo_code(self, promo_code):
        """Update a promo code on AcceptOn

        :param promo_code: The promo code to update.
        :type promo_code: PromoCode.

        :returns: PromoCode -- the updated promo code.
        :raises: accepton.Error

        :Example:

        # Updates a "SUMMERFUN" promo code to $20 off of a purchase
        >> promo_code.promo_type = "amount"
        >> promo_code.value = 2000
        >> client.update_promo_code(promo_code)
        """
        return self.perform_put_with_object(
            "/v1/promo_codes/%s" % promo_code.original_name,
            promo_code.as_params(),
            PromoCode)
