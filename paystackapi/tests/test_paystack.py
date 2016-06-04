"""Script defined to test the paystack class."""


import unittest
import httpretty

from paystackapi.paystack import Paystack
paystack_secret_key = "sk_test_0a246ef179dc841f42d20959bebdd790f69605d8"
paystack = Paystack(secret_key=paystack_secret_key)


class TestPaystackClass(unittest.TestCase):
    """Method defined to test paystack class."""

    @httpretty.activate
    def test_transaction_init(self):
        """Function defined to test dynamic class use."""
        httpretty.register_uri(
            httpretty.GET,
            "https://api.paystack.co/transaction",
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = paystack.transaction.list()
        self.assertTrue(response['status'])
