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
        return cls().requests.get('ntegration/payment_session_timeout', data=kwargs,)
