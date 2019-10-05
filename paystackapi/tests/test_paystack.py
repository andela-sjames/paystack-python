"""Script defined to test the paystack class."""

import httpretty

from paystackapi.paystack import Paystack
from paystackapi.tests.base_test_case import BaseTestCase

paystack_secret_key = "sk_test_0a246ef179dc841f42d20959bebdd790f69605d8"
paystack = Paystack(secret_key=paystack_secret_key)


class TestPaystackClass(BaseTestCase):
    """Method defined to test paystack class."""

    @httpretty.activate
    def test_transaction_init(self):
        """Method defined to test dynamic class use."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/transaction"),
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = paystack.transaction.list()
        self.assertTrue(response['status'])
