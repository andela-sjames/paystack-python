"""Entry point defined here."""
from paystackapi.customer import Customer
from paystackapi.plan import Plan
from paystackapi.product import Product
from paystackapi.subscription import Subscription
from paystackapi.subaccount import SubAccount
from paystackapi.page import Page
from paystackapi.transaction import Transaction
from paystackapi.verification import Verification
from paystackapi.misc import Misc
from paystackapi.refund import Refund

from paystackapi.base import PayStackBase


class Paystack(PayStackBase):
    """Base class defined for PayStack Instance Method."""

    def __init__(self, secret_key=None):
        """Instantiate Basic Classes to call here."""
        PayStackBase.__init__(self, secret_key=secret_key)
        self.customer = Customer
        self.plan = Plan
        self.product = Product
        self.subscription = Subscription
        self.transaction = Transaction
        self.verification = Verification
        self.misc = Misc
        self.refund = Refund
        self.subaccount = SubAccount
        self.page = Page
