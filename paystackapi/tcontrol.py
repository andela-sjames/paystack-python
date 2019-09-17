"""Script used to define the paystack Transfer Control class."""

from paystackapi.base import PayStackBase


class TransferControl(PayStackBase):
    """docstring for Transfer Control."""

    @classmethod
    def check_balance(cls):
        """
        Check Balance.

        Args:
            No argument required.

        Returns:
            Json data from paystack API.
        """

        return cls().requests.get('balance')

    @classmethod
    def resend_otp(cls, **kwargs):
        """
        Resend OTP for Transfer.

        Args:
            transfer_code: Transfer code
            reason: either resend_otp or transfer

        Returns:
            Json data from paystack API.
        """

        return cls().requests.post('transfer/resend_otp', data=kwargs,)
