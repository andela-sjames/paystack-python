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
    
    @classmethod
    def disable_otp(cls):
        """
        Disable OTP requirement for Transfers

        Args:
            No arguments required

        Returns:
            Json data from paystack API.
        """

        return cls().requests.post('transfer/disable_otp')

    @classmethod
    def disable_otp_finalize(cls, **kwargs):
        """
        Finalize Disabling of OTP requirement for Transfers

        Args:
            otp: OTP sent to business phone to verify disabling OTP requirement

        Returns:
            Json data from paystack API.
        """

        return cls().requests.post('transfer/disable_otp_finalize', data=kwargs,)

    @classmethod
    def enable_otp(cls, **kwargs):
        """
        Enable OTP requirement for Transfers

        Args:
            No arguments required

        Returns:
            Json data from paystack API.
        """

        return cls().requests.post('transfer/enable_otp', data=kwargs,)
