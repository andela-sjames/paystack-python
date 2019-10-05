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

        response = Charge.start_charge(
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
        """Method defined to test submit otp."""

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

    @httpretty.activate
    def test_submit_phone(self):
        """Method defined to test submit phone."""

        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/charge/submit_phone"),
            content_type='text/json',
            body='{"status": true, "message": "Charge attempted"}',
            status=201,
        )

        response = Charge.submit_phone(
            phone="0XX4XX9X0XF",
            reference="5bwib5v6anhe9xa",
        )

        self.assertTrue(response['status'])

    @httpretty.activate
    def test_submit_birthday(self):
        """Method defined to test submit birthday."""

        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/charge/submit_birthday"),
            content_type='text/json',
            body='{"status": true, "message": "Charge attempted"}',
            status=201,
        )

        response = Charge.submit_birthday(
            birthday="1975-12-23",
            reference="5bwib5v6anhe9xa",
        )

        self.assertTrue(response['status'])

    @httpretty.activate
    def test_check_pending(self):
        """Method defined to test check pending charge."""

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/charge/5bwib5v6anhe9xa"),
            content_type='text/json',
            body='{"status": true, "message": "Reference check successful"}',
            status=201,
        )

        response = Charge.check_pending(
            reference="5bwib5v6anhe9xa",
        )

        self.assertTrue(response['status'])
