"""Script defined to test the Class instance."""

import httpretty

from paystackapi.tests.base_test_case import BaseTestCase
from paystackapi.base import PayStackBase, PayStackRequests


class TestHttpMethods(BaseTestCase):
    """Method defined to test transaction instance."""

    def setUp(self):
        paystackbase = PayStackBase()

    @httpretty.activate
    def test_get_method_called(self):

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/transaction/4013"),
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        req = PayStackRequests()
        response = req.get('transaction/4013',)
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_post_method_called(self):

        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/transaction/charge_token"),
            content_type='text/json',
            body='{"status": true, "contributors": null}',
            status=302,
        )

        req = PayStackRequests()
        response = req.post('transaction/charge_token',
                            data={'track': 'requests'})
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_put_method_called(self):

        httpretty.register_uri(
            httpretty.PUT,
            self.endpoint_url("/customer/4013"),
            content_type='text/json',
            body='{"status": true, "contributors": null}',
            status=302,
        )

        req = PayStackRequests()
        response = req.put('customer/4013',
                           data={'test': 'requests'})
        self.assertTrue(response['status'])
