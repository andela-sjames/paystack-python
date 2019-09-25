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
        )

        response = BulkCharge.initiate_bulk_charge(


        )


        self.assertTrue(response['status'])

    @httpretty.activate
    def test_list_bulk_charges(self):
        """ """

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/bulkcharge"),

        )


        response = BulkCharge.list_bulk_charge(
            

        )

        self.assertTrue(response['status'])

    
    @httpretty.activate
    def test_fetch_bulk_charges(self):
        """ """

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/bulkcharge/{id_or_code}/charges"),
            

        )

        response = BulkCharge.list_bulk_charge(


        )

        self.assertTrue(response['status'])


    @httpretty.activate
    def test_fetch_bulk_charges(self):
        """ """

        httpretty.register_uri(

        )

        response = BulkCharge.fetch_bulk_charge(

        )

        

        self.assertTrue(responsr['status'])

    

    @httpretty.activate
    def test_pause_batch_charges(self):
        """ """

        httpretty.register_uri(

        )

        response = BulkCharge.pause_bulk_charge(

        )

        self.assertTrue(response['status'])




    @httpretty.activate
    def test_resume_batch_charges(self):
        """ """

        httpretty.register_uri(

        )

        response = BulkCharge.resume_bulk_charge(

        )

        self.assertTrue(response['status'])

