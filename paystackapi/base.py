"""Base script used across defined."""


class PayStackBase(object):
    """Base Class used across defined."""

    @classmethod
    def __init__(cls, paystack_secret_key=None):
        """Initialize Paystack with secret key."""
        cls.secret_key = paystack_secret_key
        PayStackBase.headers = {'Authorization': 'Bearer ' + cls.secret_key}
