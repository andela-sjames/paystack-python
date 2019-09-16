"""Script used to define the paystack Transaction class."""

from paystackapi.base import PayStackBase


class TransferControl(PayStackBase):
    """docstring for Transaction."""

    @classmethod
    def check_balance(cls, **kwargs):
        """
        Check Balance.

        Args:
            No argument required.

        Returns:
            Json data from paystack API.
        """

        return cls().requests.get('balance')
