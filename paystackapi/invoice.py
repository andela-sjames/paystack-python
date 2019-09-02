"""Script used to define the paystack Page class."""

from paystackapi.base import PayStackBase


class Invoice(PayStackBase):
    """docstring for Invoice."""

    @classmethod
    def create(cls, **kwargs):
        """
        Method defined to create a new invoice.

        Args:
            customer: customer id or code
            amount: payment request amount.
                    Only useful if line items and tax values are ignored.
                    Endpoint will throw a friendly warning if neither is available.
            due_date: ISO 8601 representation of request due date.
            **kwargs

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('paymentrequest', data=kwargs,)
    
    @classmethod
    def list(cls, **kwargs):
        """
        Method defined to list a new invoice.

        Args:
            customer: filter by customer ID
            status: filter by invoice status
            currency: filter by currency
            paid: filter by paid 
            include_archive: include_archive

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('paymentrequest', qs=kwargs,)
