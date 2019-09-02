"""Script used to define the paystack Control Panel class."""

from paystackapi.base import PayStackBase


class ControlPanel(PayStackBase):
    """docstring for ControlPanel."""

    @classmethod
    def fetch_payment_session_timeout(cls):
        """
        Method defined to fetch payment session timeout.

        Args:
            No argument required.

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get('integration/payment_session_timeout')
    
    @classmethod
    def update_payment_session_timeout(cls, **kwargs):
        """
        Method defined to update payment session timeout.

        Args:
            timeout: Time before stopping session (in seconds). 
                     Set to 0 to cancel session timeouts

        Returns:
            Json data from paystack API.
        """
        return cls().requests.put('integration/payment_session_timeout', data=kwargs,)
