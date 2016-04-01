"""Entry point defined here."""
from paystackapi.transaction import Transaction
from paystackapi.customer import Customer
from paystackapi.plan import Plan


class Paystack(object):
    """Base class defined for PayStack Instance Method."""

    @classmethod
    def __init__(cls, paystack_secret_key=None):
        """Instantiate Basic Classes to call here."""
        cls.transaction = Transaction(paystack_secret_key=paystack_secret_key)
        cls.customer = Customer(paystack_secret_key=paystack_secret_key)
        cls.plan = Plan(paystack_secret_key=paystack_secret_key)
