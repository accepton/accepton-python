from ..charge import Charge
from ..plan import Plan
from ..promo_code import PromoCode
from ..subscription import Subscription
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

    def plan(self, id):
        """Retrieves a plan from the API

        :param id: The plan identifier.
        :type id: str.

        :returns Plan -- The retrieved Plan.
        :raises: accepton.Error
        """
        return self.perform_get_with_object("/v1/recurring/plans/%s" % id,
                                            {},
                                            Plan)

    def plans(self, order=None, order_by=None, page=None, per_page=None):
        """Retrieves a page of plans from the API

        :param order: The order to sort by (asc or desc).
        :type order: str.
        :param order_by: The field to order by (e.g. created_at).
        :type order_by: str.
        :param page: The page number to retrieve.
        :type page: int.
        :param per_page: The size of the page to retrieve (max: 100).
        :type per_page: int.

        :returns: List<Plan> -- The list of retrieves Plans.
        :raises: accepton.Error
        """
        return self.perform_get_with_objects("/v1/recurring/plans",
                                             self.as_params(locals()),
                                             Plan)

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

    def subscription(self, id):
        """Retrieves a subscription from AcceptOn

        :param id: The subscription identifier.
        :type id: str.

        :returns: Subscription -- The retrieved Subscription.
        :raises: accepton.Error
        """
        url = "/v1/recurring/subscriptions/%s" % id
        return self.perform_get_with_object(url, {}, Subscription)

    def subscriptions(self, active=None, order=None, order_by=None, page=None,
                      per_page=None, period_unit=None, plan_token=None):
        """Retrieves a page of subscriptions from AcceptOn

        :param active: Whether to filter for active or inactive subscriptions.
        :type active: bool.
        :param order: The order to sort by (asc or desc).
        :type order: str.
        :param order_by: The field to order by (e.g. created_at).
        :type order_by: str.
        :param page: The page number to retrieve.
        :type page: int.
        :param per_page: The size of the page to retrieve (max: 100).
        :type per_page: int.
        :param plan_token: The plan id to filter by.
        :type plan_token: str.

        :raise [AcceptOn::Error]
        :returns List<Subscription> -- The list of retrieved Subscriptions.
        """
        params = self.as_params(locals())
        if params["plan_token"] is not None:
            params["plan.token"] = params["plan_token"]
            params["plan_token"] = None

        return self.perform_get_with_objects("/v1/recurring/subscriptions",
                                             params,
                                             Subscription)

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
