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
            currency: Currency type to use
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

    @classmethod
    def fetch(cls, id_or_code):
        """
        Fetch a transfer.

        Args:
            id_or_code: An ID or code for the transfer whose details you want to retrieve.

        Returns:
            Json data from paystack API.
        """

        return cls().requests.get(f"transfer/{id_or_code}")

    @classmethod
    def finalize(cls, **kwargs):
        """
        Finalize a transfer.
        NB: This step is not required if OTP is disabled

        Args:
            transfer_code: Transfer code
            otp: OTP sent to business phone to verify transfer

        Returns:
            Json data from paystack API.
        """

        return cls().requests.post('transfer/finalize_transfer', data=kwargs)

    @classmethod
    def initiate_bulk_transfer(cls, **kwargs):
        """
        Initiate bulk transfer.

        Args:
            currency: Currency type to use
            source: Where should we transfer from? Only balance for now
            transfers: Array of transfer objects [
                { 
                    amount: Amount to transfer in kobo
                    recipient: Code for transfer recipient
                },
                {
                    amount: Amount to transfer in kobo
                    recipient: Code for transfer recipient
                }
            ]

        Returns:
            Json data from paystack API.
        """

        return cls().requests.post('transfer/bulk', data=kwargs)

    @classmethod
    def verify(cls, reference):
        """
        Verify a transfer.

        Args:
            reference: Transfer reference

        Returns:
            Json data from paystack API.
        """

        return cls().requests.get(f"verify/{reference}")
