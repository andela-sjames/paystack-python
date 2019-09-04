import httpretty

from paystackapi.tests.base_test_case import BaseTestCase
from paystackapi.invoice import Invoice


class TestInvoice(BaseTestCase):

    @httpretty.activate
    def test_create_invoice(self):
        """Method defined to test create Invoice."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/paymentrequest"),
            content_type='text/json',
            body='{"status": true, "message": "Invoice created"}',
            status=201,
        )

        response = Invoice.create(
            customer="CUS_je02lbimlqixzax",
            amount=42000,
            due_date="2019-05-08T00:00:00.000Z"
        )
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_list_invoice(self):
        """Method defined to test list Invoice."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/paymentrequest"),
            content_type='text/json',
            body='{"status": true, "message": "Invoice retrieved"}',
            status=201,
        )

        response = Invoice.list(
            customer="CUS_je02lbimlqixzax",
            status="pending",
            currency="NGN",
            paid="false",
            include_archive="true"
        )
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_view_invoice(self):
        """Method defined to test view Invoice."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/paymentrequest/PRQ_kp4lleqc7g8xckk"),
            content_type='text/json',
            body='{"status": true, "message": "Invoice retrieved"}',
            status=201,
        )

        response = Invoice.view(
            invoice_id_or_code="PRQ_kp4lleqc7g8xckk",
        )
        self.assertTrue(response['status'])
    
    @httpretty.activate
    def test_verify_invoice(self):
        """Method defined to test verify Invoice."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/paymentrequest/verify/PRQ_kp4lleqc7g8xckk"),
            content_type='text/json',
            body='{"status": true, "message": "Payment request retrieved"}',
            status=201,
        )

        response = Invoice.verify(
            invoice_code="PRQ_kp4lleqc7g8xckk",
        )
        self.assertTrue(response['status'])