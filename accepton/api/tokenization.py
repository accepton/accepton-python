from ..transaction_token import TransactionToken
from .utils import Utils


class Tokenization(Utils):
    def create_token(self, amount=None, application_fee=None, currency="usd",
                     description=None, merchant_paypal_account=None):
        """Create a transaction token on AcceptOn

        :param amount: The amount in cents of the transaction.
        :type amount: int.
        :param application_fee: The fee in cents to pass on to the marketplace.
        :type application_fee: int.
        :param currency: The currency to charge in (default: usd).
        :type currency: str.
        :param description: A description of the transaction.
        :type description: str.
        :param merchant_paypal_account: The merchant's Paypal account when you
                                        want to pay a merchant instead of
                                        yourself. Can be used with an
                                        application fee.
        :type merchant_paypal_account: str.

        :returns: TransactionToken -- The created TransactionToken.
        :raises: accepton.Error

        :Example:

        # Create a transaction token with an amount of $1.00.
        >> client.create_token(amount=100)

        # Create a transaction token with a description (from a dict).
        >> client.create_token(**{"amount": 100, "description": "Test"})

        # Create a transaction token with a description and application fee.
        >> client.create_token(amount=1099, description="Test",
                               application_fee=99)

        # Create a Paypal-specific token that pays a merchant and charges them
        # an application fee.
        >> client.create_token(amount=15_00, description="Test",
                               application_fee=150,
                               merchant_paypal_account="merchant@example.com")
        """
        return self.perform_post_with_object("/v1/tokens",
                                             self.as_params(locals()),
                                             TransactionToken)
