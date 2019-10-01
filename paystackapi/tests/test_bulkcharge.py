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
                batch_code="BCH_180tl7oq7cayggh",
        )


        self.assertTrue(response['status'])

    @httpretty.activate
    def test_list_bulk_charge(self):
        """ """

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/bulkcharge"),
            content_type='application/json',
            body = '{"status": true, "message": "Bulk charges retrieved",}',
            status=200,
        )


        response = BulkCharge.list_bulk_charge(

            

        )

        self.assertTrue(response['status'])

    
    @httpretty.activate
    def test_fetch_bulk_charge_batch(self):
        """ """

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/bulkcharge/{id_or_code}/charges"),
            content_type='text/json',
            body = '{"status": true, "message": "Bulk charges retrieved",}',
            status=200,
        )

        response = BulkCharge.fetch_bulk_charge_batch(
            batch_code= "BCH_180tl7oq7cayggh",
        )

        self.assertTrue(response['status'])


    @httpretty.activate
    def test_fetch_charges(self):
        """ """

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/bulkcharge/BCH_180tl7oq7cayggh/charges"),
            content_type= 'text/json',
            body='{"status": true, "message": "Bulk charge items retrieved",}',
            status=200,
        )

        response = BulkCharge.fetch_charges(

        )

        
        self.assertTrue(response['status'])

    

    @httpretty.activate
    def test_pause_batch_charges(self):
        """ """

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("bulkcharge/pause/BCH_180tl7oq7cayggh"),
            content_type='text/json',
            body='{""status": true, "message": "Bulk charge batch has been paused""}',
            status=201,
        )

        response = BulkCharge.pause_bulk_charge(


        )

        self.assertTrue(response['status'])




    @httpretty.activate
    def test_resume_batch_charges(self):
        """ """

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("bulkcharge/resume/BCH_180tl7oq7cayggh"),
            content_type='text/json',
            body='{"status": true, "message": "Bulk charge batch has been resumed"}',
            status=201,
        )

        response = BulkCharge.resume_bulk_charge(


        )

        self.assertTrue(response['status'])

