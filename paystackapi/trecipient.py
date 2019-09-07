"""Script used to define the paystack Transfer Recipient class."""

from paystackapi.base import PayStackBase


class TransferRecipient(PayStackBase):
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
    
    @classmethod
    def list(cls, **kwargs):
        """
        Method defined to list transfer recipient.

        Args:
            perPage: records you want to retrieve per page (Integer)
            page: what page you want to retrieve (Integer)

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get('transferrecipient', qs=kwargs,)
