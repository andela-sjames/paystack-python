"""Script used to define the paystack Verification class."""

from paystackapi.base import PayStackBase


class Verification(PayStackBase):
    """docstring for Verification."""

    @classmethod
    def verify_bvn(cls, **kwargs):
        """
        Verify BVN

        Args:
            bvn:        customer's BVN number

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get('bank/resolve_bvn/{bvn}'.format(**kwargs))

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
        return cls().requests.get(
          'bank/resolve?account_number={account_number}&bank_code={bank_code}'
          .format(**kwargs))

    @classmethod
    def verify_card_bin(cls, **kwargs):
        """
        Verify card bin

        Args:
            card_bin:           customer's card bin number

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get('decision/bin/{card_bin}'.format(**kwargs))

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
