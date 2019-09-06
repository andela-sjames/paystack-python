"""Script used to define the paystack Transfer Recipient class."""

from paystackapi.base import PayStackBase


class Invoice(PayStackBase):
    """docstring for Transfer Recipient."""

    @classmethod
    def create(cls, **kwargs):
        """
        Method defined to create transfer recipient.

        Args:
            type: Recipient Type (Only nuban at this time)
            name: A name for the recipient
            account_number: Required if type is nuban
            bank_code: Required if type is nuban. 
                       You can get the list of Bank Codes by calling the List Banks endpoint.
            **kwargs

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('transferrecipient', data=kwargs,)
