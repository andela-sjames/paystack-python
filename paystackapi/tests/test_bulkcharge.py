import httpretty

from paystackapi.tests.base_test_case import BaseTestCase
from paystackapi.bulkcharge import BulkCharge

class TestBulkCharge(BaseTestCase):

    @httpretty.activate
    def test_initiate_bulk_charge(self):
        """ Method for testing the initiation of a bulk charge"""

        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/bulkcharge"),
            content_type='applicationn/json',
            body='{"status": true, "message": "Charges have been queued"}',
            status=200,
        )

        response = BulkCharge.initiate_bulk_charge(
            bulkcharge=[
                {"authorization": "AUTH_n95vpedf", "amount": 2500}, 
                {"authorization": "AUTH_ljdt4e4j", "amount": 1500}
            ]
        )

        self.assertTrue(response['status'])

    @httpretty.activate
    def test_list(self):
        """ """

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/bulkcharge"),
            content_type='application/json',
            body ='{"status": true, "message": "Bulk charges retrieved"}',
            status=200,
        )

        response = BulkCharge.list()
        self.assertTrue(response['status'])
    
    @httpretty.activate
    def test_fetch_bulk_batch(self):
        """ """

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/bulkcharge/BCH_orj0ttn8vtp80hx"),
            content_type='text/json',
            body='{"status": true, "message": "Bulk charges retrieved"}',
            status=200,
        )

        response = BulkCharge.fetch_bulk_batch(
            id_or_code="BCH_orj0ttn8vtp80hx"
        )

        self.assertTrue(response['status'])

    @httpretty.activate
    def test_fetch_charges_batch(self):
        """ """

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/bulkcharge/BCH_orj0ttn8vtp80hx/charges"),
            content_type= 'text/json',
            body='{"status": true, "message": "Bulk charge items retrieved"}',
            status=200,
        )

        response = BulkCharge.fetch_charges_batch(
            id_or_code="BCH_orj0ttn8vtp80hx"
        )

        self.assertTrue(response['status'])

    @httpretty.activate
    def test_pause_bulk_batch(self):
        """ """

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("bulkcharge/pause/BCH_orj0ttn8vtp80hx"),
            content_type='text/json',
            body='{"status": true, "message": "Bulk charge batch has been paused"}',
            status=201,
        )

        response = BulkCharge.pause_bulk_batch(
            batch_code="BCH_orj0ttn8vtp80hx"
        )
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_resume_batch_charges(self):
        """ """

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("bulkcharge/resume/BCH_orj0ttn8vtp80hx"),
            content_type='text/json',
            body='{"status": true, "message": "Bulk charge batch has been resumed"}',
            status=201,
        )

        response = BulkCharge.resume_bulk_charge(
            batch_code="BCH_orj0ttn8vtp80hx"
        )

        self.assertTrue(response['status'])
