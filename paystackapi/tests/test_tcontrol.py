import httpretty

from paystackapi.tests.base_test_case import BaseTestCase
from paystackapi.tcontrol import TransferControl


class TestTransfer(BaseTestCase):

    @httpretty.activate
    def test_check_balance(self):
        """Method defined to test check_balance."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/balance"),
            content_type='text/json',
            body='{"status": true, "message": "Balances retrieved"}',
            status=201,
        )

        response = TransferControl.check_balance()
        self.assertTrue(response['status'])
