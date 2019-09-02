import httpretty

from paystackapi.tests.base_test_case import BaseTestCase
from paystackapi.cpanel import ControlPanel


class TestPage(BaseTestCase):

    @httpretty.activate
    def test_fetch_payment_session_timeout(self):
        """Method defined to test fetch payment session timeout."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/integration/payment_session_timeout"),
            content_type='text/json',
            body='{"status": true, "message": "Payment session timeout retrieved"}',
            status=201,
        )

        response = ControlPanel.fetch_payment_session_timeout()
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_update_payment_session_timeout(self):
        """Method defined to test update payment session timeout."""
        httpretty.register_uri(
            httpretty.PUT,
            self.endpoint_url("/integration/payment_session_timeout"),
            content_type='text/json',
            body='{"status": true, "message": "Payment session timeout updated"}',
            status=201,
        )

        response = ControlPanel.update_payment_session_timeout(timeout=30)
        self.assertTrue(response['status'])
