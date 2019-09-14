"""Script used to define the paystack Transfer class."""

from paystackapi.base import PayStackBase


class Transfer(PayStackBase):
    """docstring for Transaction."""

    @classmethod
    def initiate(cls, **kwargs):
        """
        Initialize a transfer.

        Args:
            source: Where should we transfer from? Only balance for now
            amount: Amount to transfer in kobo
            recipient: Code for transfer recipient

        Returns:
            Json data from paystack API.
        """

        return cls().requests.post('transfer', data=kwargs)
