from ..charge import Charge
from ..promo_code import PromoCode
from ..transaction_token import TransactionToken
from .utils import Utils


class Querying(Utils):
    def charge(self, id):
        """Retrieves a charge from the API

        :param id: The charge identifier.
        :type id: str.

        :returns Charge -- The retrieved Charge.
        :raises: accepton.Error
        """
        return self.perform_get_with_object("/v1/charges/%s" % id,
                                            {},
                                            Charge)

    def charges(self, start_date=None, end_date=None, order_by=None,
                order=None):
        """Retrieves a page of charges from the API

        :param start_date: The earliest date for the objects to be created.
        :type start_date: datetime.datetime, str.
        :param end_date: The latest date for the objects to be created.
        :type end_date: datetime.datetime, str.
        :param order: The order to sort by (asc or desc).
        :type order: str.
        :param order_by: The field to order by (e.g. created_at).
        :type order_by: str.

        :returns: List<Charge> -- The list of retrieves Charges.
        :raises: accepton.Error
        """
        return self.perform_get_with_objects("/v1/charges",
                                             self.as_params(locals()),
                                             Charge)

    def promo_code(self, name):
        """Retrieve a promo code from AcceptOn

        :param name: The name of the promo code to retrieve.
        :type name: str.

        :returns: PromoCode -- The retrieved promo code.
        :raises: accepton.Error

        :Example:

        # Retrieve the promo code with the name "20OFF"
        >> client.promo_code("20OFF")
        """
        return self.perform_get_with_object("/v1/promo_codes/%s" % name,
                                            {},
                                            PromoCode)

    def promo_codes(self, order=None, order_by=None, page=None, per_page=None,
                    promo_type=None):
        """Retrieves a page of promo codes from the API

        :param order: The order to sort by (asc or desc).
        :type order: str.
        :param order_by: The field to order by (e.g. created_at).
        :type order_by: str.
        :param page: The page number to retrieve.
        :type page: int.
        :param per_page: The size of the page to retrieve (max: 100).
        :type per_page: int.
        :param promo_type: The type of promo code to filter by.
        :type promo_type: str.

        :returns: List<PromoCode> -- The list of retrieved PromoCodes.
        :raises: accepton.Error
        """
        return self.perform_get_with_objects("/v1/promo_codes",
                                             self.as_params(locals()),
                                             PromoCode)

    def token(self, id):
        """Retrieves a transaction token from the API

        :param id: The transaction token identifier.
        :type id: str.

        :returns TransactionToken -- The retrieved TransactionToken.
        :raises: accepton.Error
        """
        return self.perform_get_with_object("/v1/tokens/%s" % id,
                                            {},
                                            TransactionToken)
