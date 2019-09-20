import httpretty

from paystackapi.tests.base_test_case import BaseTestCase
from paystackapi.tcontrol import TransferControl


class TestTransferControl(BaseTestCase):

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

    @httpretty.activate
    def test_resend_otp(self):
        """Method defined to test resend_otp."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/transfer/resend_otp"),
            content_type='text/json',
            body='{"status": true, "message": "OTP has been resent"}',
            status=201,
        )

        response = TransferControl.resend_otp(
            transfer_code="TRF_vsyqdmlzble3uii",
            reason="Just do it."
        )
        self.assertTrue(response['status'])
    
    @httpretty.activate
    def test_disable_otp(self):
        """Method defined to test disable_otp."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/transfer/disable_otp"),
            content_type='text/json',
            body='{"status": true,\
                "message": "OTP has been sent to mobile number ending with 4321"}',
            status=201,
        )

        response = TransferControl.disable_otp()
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_disable_otp_finalize(self):
        """Method defined to test disable_otp_finalize."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/transfer/disable_otp_finalize"),
            content_type='text/json',
            body='{"status": true,\
                "message": "OTP requirement for transfers has been disabled"}',
            status=201,
        )

        response = TransferControl.disable_otp_finalize(
            otp="928783",
        )
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_enable_otp(self):
        """Method defined to test enable_otp."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/transfer/enable_otp"),
            content_type='text/json',
            body='{"status": true,\
                "message": "OTP requirement for transfers has been enabled"}',
            status=201,
        )

        response = TransferControl.enable_otp()
        self.assertTrue(response['status'])
