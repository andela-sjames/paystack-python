"""Script defined to test the Class instance."""


import unittest
import httpretty

from paystackapi.base import PayStackBase, PayStackRequests


class TestHttpMethods(unittest.TestCase):
    """Method defined to test transaction instance."""

    def setUp(self):
        paystackbase = PayStackBase()

    @httpretty.activate
    def test_get_method_called(self):

        httpretty.register_uri(
            httpretty.GET,
            "https://api.paystack.co/transaction/4013",
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
            "https://api.paystack.co/transaction/charge_token",
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
            "https://api.paystack.co/customer/4013",
            content_type='text/json',
            body='{"status": true, "contributors": null}',
            status=302,
        )

        req = PayStackRequests()
        response = req.put('customer/4013',
                           data={'test': 'requests'})
        self.assertTrue(response['status'])
