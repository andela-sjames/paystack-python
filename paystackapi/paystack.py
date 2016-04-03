"""Entry point defined here."""
from paystackapi.transaction import Transaction
from paystackapi.customer import Customer
from paystackapi.plan import Plan
from paystackapi.base import PayStackBase


class Paystack(PayStackBase):
    """Base class defined for PayStack Instance Method."""

    def __init__(self, secret_key=None):
        """Instantiate Basic Classes to call here."""
        PayStackBase.__init__(self, secret_key=secret_key)
        self.transaction = Transaction
        self.customer = Customer
        self.plan = Plan
