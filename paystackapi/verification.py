"""Script used to define the paystack Verification class."""

from paystackapi.base import PayStackBase


class Verification(PayStackBase):
    """docstring for Verification."""

    @classmethod
    def verify_bvn(cls, bvn):
        """
        Verify BVN

        Args:
            bvn:        customer's BVN number

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get(f"bank/resolve_bvn/{bvn}")

    @classmethod
    def verify_account(cls, **kwargs):
        """
        Verify account

        Args:
            account_number:     customer's account number
            bank_code:          customer's bank code

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get("bank/resolve", qs=kwargs,)

    @classmethod
    def verify_card_bin(cls, card_bin):
        """
        Verify card bin

        Args:
            card_bin:           customer's card bin number

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get(f"decision/bin/{card_bin}")

    @classmethod
    def verify_phone(cls, **kwargs):
        """
        Verify customer phone number

        Args:
            verification_type:      phone verification type
            phone:                  customer's phone number
            callback_url:           url to receive verification details

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('verifications', data=kwargs)
