"""Script used to define the paystack Transaction class."""

from paystackapi.base import PayStackBase


class Transaction(PayStackBase):
    """docstring for Transaction."""

    @classmethod
    def initialize(cls, **kwargs):
        """
        Initialize transaction.

        Args:
            reference: unique transaction reference
            amount: amount
            email: email address
            plan: specified plan(optional)

        Returns:
            Json data from paystack API.
        """

        return cls().requests.post('transaction/initialize', data=kwargs)

    @classmethod
    def charge(cls, **kwargs):
        """
        Charge authorization.

        Args:
            reference: Unique transaction reference
            authorization_code: Authorization code for the transaction
            email: Email Address of the user with the authorization code
            amount: Amount in kobo

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('transaction/charge_authorization',
                                   data=kwargs)

    @classmethod
    def charge_token(cls, **kwargs):
        """
        Charge token.

        Args:
            reference: unique transaction reference
            token: paystack token
            email: Email Address
            amount: Amount in Kobo

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('transaction/charge_token', data=kwargs)

    @classmethod
    def get(cls, transaction_id):
        """
        Get a single transaction.

        Args:
            transaction_id: Transaction id(integer).

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get(f"transaction/{transaction_id}")

    @classmethod
    def list(cls):
        """
        List transactions.

        Args:
            No argument required.

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get('transaction')

    @classmethod
    def totals(cls):
        """
        Get totals.

        Args:
            No argument required.

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get('transaction/totals')

    @classmethod
    def verify(cls, reference):
        """
        Verify transactions.

        Args:
            reference: a unique value needed for transaction.

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get(f"transaction/verify/{reference}")
