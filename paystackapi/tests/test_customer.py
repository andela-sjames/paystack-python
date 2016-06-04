"""Script defined to test the Customer class."""


import unittest
import httpretty

from paystackapi.customer import Customer


class TestCustomer(unittest.TestCase):
    """Class to test customer actions."""

    @httpretty.activate
    def test_create(self):
        """Method defined to test customer creation."""
        httpretty.register_uri(
            httpretty.POST,
            "https://api.paystack.co/customer",
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Customer.create(
            first_name='samuel', last_name='james',
            email='johndoe@andela.com', phone='00000000000')
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_get(self):
        """Function defined to test Customer get method."""
        httpretty.register_uri(
            httpretty.GET,
            "https://api.paystack.co/customer/4013",
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Customer.get(customer_id=4013)
        self.assertEqual(response['status'], True)

    @httpretty.activate
    def test_list(self):
        """Function defined to test paystackapi customer list method."""
        httpretty.register_uri(
            httpretty.GET,
            "https://api.paystack.co/customer",
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Customer.list()
        self.assertEqual(response['status'], True)

    @httpretty.activate
    def test_update(self):
        """Function defined to test paystackapi customer update."""
        httpretty.register_uri(
            httpretty.PUT,
            "https://api.paystack.co/customer/4013",
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Customer.update(customer_id=4013, first_name='andela')
        self.assertEqual(response['status'], True)
