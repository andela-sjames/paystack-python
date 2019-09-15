import httpretty

from paystackapi.tests.base_test_case import BaseTestCase
from paystackapi.transfer import Transfer


class TestTransfer(BaseTestCase):

    @httpretty.activate
    def test_initiate(self):
        """Method defined to test transfer initiation."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/transfer"),
            content_type='text/json',
            body='{"status": true, "message": "Transfer requires OTP to continue"}',
            status=201,
        )

        response = Transfer.initiate(
            source="balance",
            reason="Calm down",
            amount="3794800",
            recipient="RCP_gx2wn530m0i3w3m",
        )
        self.assertTrue(response['status'])
