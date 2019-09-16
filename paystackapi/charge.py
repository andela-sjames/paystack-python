"""Script used to define the paystack Charge class."""

from paystackapi.base import PayStackBase


class Charge(PayStackBase):
    """docstring for Charge."""

    @classmethod
    def charge(cls, **kwargs):
        """
        Method defined to start a charge.

        Args:
            email: Customer's email address
            amount: Amount in kobo

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('charge', data=kwargs,)
