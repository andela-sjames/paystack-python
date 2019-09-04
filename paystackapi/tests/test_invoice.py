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
    
    @httpretty.activate
    def test_send_notifications(self):
        """Method defined to test notifications Invoice."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/paymentrequest/notify/PRQ_kp4lleqc7g8xckk"),
            content_type='text/json',
            body='{"status": true}',
            status=201,
        )

        response = Invoice.send_notification(
            id_or_code="PRQ_kp4lleqc7g8xckk",
        )
        self.assertTrue(response['status'])
    
    @httpretty.activate
    def test_dashboard_metrics(self):
        """Method defined to test Invoice dashboard metrics."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/paymentrequest/totals"),
            content_type='text/json',
            body='{"status": true}',
            status=201,
        )

        response = Invoice.dashboard_metrics()
        self.assertTrue(response['status'])
    
    @httpretty.activate
    def test_finalize_draft(self):
        """Method defined to test finalize_draft Invoice."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/paymentrequest/finalize/PRQ_kp4lleqc7g8xckk"),
            content_type='text/json',
            body='{"status": true}',
            status=201,
        )

        response = Invoice.finalize_draft(
            id_or_code="PRQ_kp4lleqc7g8xckk",
            send_notification=False
        )
        self.assertTrue(response['status'])
    
    @httpretty.activate
    def test_update(self):
        """Method defined to test Invoice update."""
        httpretty.register_uri(
            httpretty.PUT,
            self.endpoint_url("/paymentrequest/PRQ_kp4lleqc7g8xckk"),
            content_type='text/json',
            body='{"status": true, "message": "Payment request updated"}',
            status=201,
        )

        response = Invoice.update(
            id_or_code="PRQ_kp4lleqc7g8xckk",
            amount=450000
        )
        self.assertTrue(response['status'])
    
    @httpretty.activate
    def test_archive(self):
        """Method defined to test Invoice archive."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/invoice/archive/PRQ_kp4lleqc7g8xckk"),
            content_type='text/json',
            body='{"status": true, "message": "Payment request archived"}',
            status=201,
        )

        response = Invoice.archive(
            id_or_code="PRQ_kp4lleqc7g8xckk",
        )
        self.assertTrue(response['status'])
    
    @httpretty.activate
    def test_update_transfer_recipient(self):
        """Method defined to test Invoice archive."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/transferrecipient/PRQ_kp4lleqc7g8xckk"),
            content_type='text/json',
            body='{"status": true}',
            status=201,
        )

        response = Invoice.update_transfer_recipient(
            recipient_code_or_id="PRQ_kp4lleqc7g8xckk",
            name="new name",
            email="new@email.com"
        )
        self.assertTrue(response['status'])

