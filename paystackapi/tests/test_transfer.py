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

    @httpretty.activate
    def test_list(self):
        """Method defined to test transfer list."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/transfer"),
            content_type='text/json',
            body='{"status": true, "message": "Transfers retrieved"}',
            status=201,
        )

        response = Transfer.list(
            perPage=3,
            page=1
        )
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_fetch(self):
        """Method defined to test transfer fetch."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/transfer/TRF_2x5j67tnnw1t98k"),
            content_type='text/json',
            body='{"status": true, "message": "Transfers retrieved"}',
            status=201,
        )

        response = Transfer.fetch(
            id_or_code="TRF_2x5j67tnnw1t98k",
        )

        self.assertTrue(response['status'])
