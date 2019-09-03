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
            paid: filter by paid invoice
            include_archive: include_archive

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get('paymentrequest', qs=kwargs,)

    @classmethod
    def view(cls, invoice_id_or_code):
        """
        Method defined to view an invoice

        Args:
            invoice_id_or_code: invoice ID or Code (string)

        Returns:
            Json data from paystack API.
        """
            return cls().requests.get('paymentrequest/{invoice_id_or_code}')

    @classmethod
    def verify(cls, invoice_code):
        """
        Method defined to verify an invoice

        Args:
            invoice_code: invoice Code (string)

        Returns:
            Json data from paystack API.
        """
            return cls().requests.get('paymentrequest/verify/{invoice_code}')

    @classmethod
    def send_notification(cls, id_or_code):
        """
        Method defined to send notification

        Args:
            id_or_code: id or code (string)

        Returns:
            Json data from paystack API.
        """
            return cls().requests.post('paymentrequest/notify/{id_or_code}')

    @classmethod
    def dashboard_metrics(cls):
        """
        Method defined to get Dashboard metrics.

        Args:
            No Arguments required

        Returns:
            Json data from paystack API.
        """
            return cls().requests.get('paymentrequest/totals')

    @classmethod
    def finalize_draft(cls, id_or_code):
        """
        Method defined to finalize a draft.

        Args:
            id_or_code: ID or Code (string)

        Returns:
            Json data from paystack API.
        """
            return cls().requests.post('paymentrequest/finalize/{id_or_code}')

    @classmethod
    def update(cls, id_or_code, **kwargs):
        """
        Method defined to update a draft.

        Args:
            id_or_code: ID or Code

        Returns:
            Json data from paystack API.
        """
            return cls().requests.put('paymentrequest/{id_or_code}', data=kwargs)

    