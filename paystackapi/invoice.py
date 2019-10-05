"""Script used to define the paystack Invoice class."""

from paystackapi.base import PayStackBase


class Invoice(PayStackBase):
    """docstring for Invoice."""

    @classmethod
    def create(cls, **kwargs):
        """
        Method defined to create a new invoice.

        Args:
            customer: customer id or code
            amount: payment request amount.(Integer)
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
        return cls().requests.get(f'paymentrequest/{invoice_id_or_code}')

    @classmethod
    def verify(cls, invoice_code):
        """
        Method defined to verify an invoice

        Args:
            invoice_code: invoice Code (string)

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get(f'paymentrequest/verify/{invoice_code}')

    @classmethod
    def send_notification(cls, id_or_code):
        """
        Method defined to send notification

        Args:
            id_or_code: id or code (string)

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post(f'paymentrequest/notify/{id_or_code}')

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
    def finalize_draft(cls, id_or_code, **kwargs):
        """
        Method defined to finalize a draft.

        Args:
            id_or_code: ID or Code (string)
            send_notification: Indicates whether Paystack sends an email notification to customer.
                Defaults to true. (Boolean)

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post(f'paymentrequest/finalize/{id_or_code}', data=kwargs)

    @classmethod
    def update(cls, id_or_code, **kwargs):
        """
        Method defined to update a draft.

        Args:
            id_or_code: ID or Code
            **kwargs

        Returns:
            Json data from paystack API.
        """
        return cls().requests.put(f'paymentrequest/{id_or_code}', data=kwargs)

    @classmethod
    def archive(cls, id_or_code):
        """
        Method defined to archive a draft.

        Args:
            id_or_code: ID or Code

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post(f'invoice/archive/{id_or_code}')

    @classmethod
    def update_transfer_recipient(cls, recipient_code_or_id, **kwargs):
        """
        Method defined to Update transfer recipient a draft.

        Args:
            recipient_code_or_id: recipient code or ID
            name: a name for the recipient (string)
            email: the email address of the recipient (string)

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post(f'transferrecipient/{recipient_code_or_id}', data=kwargs)
