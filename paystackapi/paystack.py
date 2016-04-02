"""Entry point defined here."""
from paystackapi.transaction import Transaction
from paystackapi.customer import Customer
from paystackapi.plan import Plan


class Paystack(object):
    """Base class defined for PayStack Instance Method."""

    @classmethod
    def __init__(cls, secret_key=None):
        """Instantiate Basic Classes to call here."""
        cls.transaction = Transaction
        cls.customer = Customer
        cls.plan = Plan
