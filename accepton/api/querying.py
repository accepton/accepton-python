from ..charge import Charge
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
