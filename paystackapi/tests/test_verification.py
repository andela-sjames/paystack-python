"""Script defined to test the Verification class."""

import httpretty

from paystackapi.verification import Verification
from paystackapi.tests.base_test_case import BaseTestCase


class TestVerification(BaseTestCase):
    """Class to test verification actions."""

    @httpretty.activate
    def test_verify_bvn(self):
        """Method defined to test bvn verification."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/bank/resolve_bvn/01234567689"),
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=200,
        )

        response = Verification.verify_bvn(bvn='01234567689')
        self.assertTrue(response['status'])

    
    @httpretty.activate
    def test_verify_bvn_match(self):
        """Method defined to test bvn match verification."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/bank/resolve"),
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Verification.verify_bvn_match(
            bvn='01234567689', 
            account_number='123456',
            bank_code='093')
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_verify_account(self):
        """Method defined to test account number verification."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/bank/resolve?account_number=123456&bank_code=093"),
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=200,
        )

        response = Verification.verify_account(
            account_number='123456', bank_code='093')
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_verify_card_bin(self):
        """Method defined to test card bin verification."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/decision/bin/1234565"),
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=200,
        )

        response = Verification.verify_card_bin(card_bin='1234565')
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_verify_phone(self):
        """Method defined to test phone number verification."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/verifications"),
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Verification.verify_phone(
            verification_type='truecaller',
            phone='09192039203',
            callback_url='https://google.com'
        )
        self.assertTrue(response['status'])
