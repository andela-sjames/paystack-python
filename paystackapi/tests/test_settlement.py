import httpretty

from paystackapi.tests.base_test_case import BaseTestCase
from paystackapi.settlement import Settlement


class TestPage(BaseTestCase):

    @httpretty.activate
    def test_page_fetch(self):
        """Method defined to test fetch."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/settlement"),
            content_type='text/json',
            body='{"status": true, "message": "Settlements retrieved"}',
            status=201,
        )

        response = Settlement.fetch(
            start_date="2016-09-12T00:00:00.000Z",
            end_date="2016-09-12T00:00:00.000Z",
            subaccount="subaccount"
        )
        self.assertEqual(response['status'], True)
