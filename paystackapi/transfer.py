"""Script used to define the paystack Transfer class."""

from paystackapi.base import PayStackBase


class Transfer(PayStackBase):
    """docstring for Transfer."""

    @classmethod
    def initiate(cls, **kwargs):
        """
        Initiate a transfer.

        Args:
            source: Where should we transfer from? Only balance for now
            amount: Amount to transfer in kobo
            recipient: Code for transfer recipient

        Returns:
            Json data from paystack API.
        """

        return cls().requests.post('transfer', data=kwargs)

    @classmethod
    def list(cls, **kwargs):
        """
        List a transfer.

        Args:
            perPage: records you want to retrieve per page (Integer)
            page: what page you want to retrieve (Integer)

        Returns:
            Json data from paystack API.
        """

        return cls().requests.get('transfer', qs=kwargs,)
