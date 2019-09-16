import httpretty

from paystackapi.tests.base_test_case import BaseTestCase
from paystackapi.charge import Charge


class TestCharge(BaseTestCase):

    @httpretty.activate
    def test_start_charge(self):
        """Method defined to test start charge."""

        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/charge"),
            content_type='text/json',
            body='{"status": true, "message": "Charge attempted"}',
            status=201,
        )

        response = Charge.charge(
            email="CUS_je02lbimlqixzax",
            amount=42000,
            metadata={
                "custom_fields": [
                    {
                        "value":"makurdi",
                        "display_name": "Donation for",
                        "variable_name": "donation_for"
                    },
                ],
            },
            bank={
                "code":"057",
                "account_number":"0000000000"
            },
            birthday="1995-12-23"
        )

        self.assertTrue(response['status'])

    @httpretty.activate
    def test_submit_pin(self):
        """Method defined to test submit pin."""

        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/charge/submit_pin"),
            content_type='text/json',
            body='{"status": true, "message": "Charge attempted"}',
            status=201,
        )

        response = Charge.submit_pin(
            pin="0987",
            reference="5bwib5v6anhe9xa",
        )

        self.assertTrue(response['status'])

    @httpretty.activate
    def test_submit_otp(self):
        """Method defined to test submit pin."""

        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/charge/submit_otp"),
            content_type='text/json',
            body='{"status": true, "message": "Charge attempted"}',
            status=201,
        )

        response = Charge.submit_otp(
            otp="0987",
            reference="5bwib5v6anhe9xa",
        )

        self.assertTrue(response['status'])
