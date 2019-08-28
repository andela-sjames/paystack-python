import httpretty

from paystackapi.tests.base_test_case import BaseTestCase
from paystackapi.subaccount import SubAccount


class TestSubAccount(BaseTestCase):

    @httpretty.activate
    def test_subaccount_create(self):
        pass

        """Method defined to test subaccount creation."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/subaccount"),
            content_type='text/json',
            body='{"status": true, "message": "Subaccount created"}',
            status=201,
        )

        response = SubAccount.create(
            business_name="Test Biz 123", settlement_bank="Access Bank",
            account_number="xxxxxxxxx", percentage_charge="6.9"
        )
        self.assertTrue(response['status'])
