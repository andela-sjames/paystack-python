import httpretty

from paystackapi.tests.base_test_case import BaseTestCase
from paystackapi.trecipient import TransferRecipient


class TestSubAccount(BaseTestCase):

    @httpretty.activate
    def test_create_trecipient(self):
        """Method defined to test trecipient creation."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/transferrecipient"),
            content_type='text/json',
            body='{"status": true, "message": "Recipient created"}',
            status=201,
        )

        response = TransferRecipient.create(
            type="nuban",
            name="Zombie",
            description="Zombier",
            account_number="01000000010",
            bank_code="044",
        )
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_list_trecipient(self):
        """Method defined to test trecipient list."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/transferrecipient"),
            content_type='text/json',
            body='{"status": true, "message": "Recipient retrieved"}',
            status=201,
        )

        response = TransferRecipient.list(perPage=3, page=1)
        self.assertEqual(response['status'], True)