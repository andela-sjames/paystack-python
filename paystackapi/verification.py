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
    def verify_bvn_match(cls, **kwargs):
        """
        Verify bvn match with account number, first name and last name
        Args:
            bvn:                customer's bvn
            account_number:     customer's account number
            bank_code:          customer's bank code
            first_name:         customer's first name (Optional)
            last_name:          customer's last name (Optional)
            middle_name:        customer's middle name (Optional)
        Returns:
            Json data from paystack API.
            {
              "status": true,
              "message": "BVN lookup successful",
              "data": {
                "bvn": "xxxxxxxxxxx",
                "is_blacklisted": false,
                "account_number": true,
                "first_name": true,
                "middle_name": false,
                "last_name": true
              },
              "meta": {
                "calls_this_month": 1,
                "free_calls_left": 9
              }
            }
        """
        return cls().requests.post('bank/resolve', data=kwargs)

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
