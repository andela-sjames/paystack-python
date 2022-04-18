"""Script defined to test the Customer class."""

import httpretty

from paystackapi.tests.base_test_case import BaseTestCase
from paystackapi.customer import Customer


class TestCustomer(BaseTestCase):
    """Class to test customer actions."""

    @httpretty.activate
    def test_create(self):
        """Method defined to test customer creation."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/customer"),
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
        """Method defined to test Customer get."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/customer/4013"),
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Customer.get(customer_id=4013)
        self.assertEqual(response['status'], True)

    @httpretty.activate
    def test_list(self):
        """Method defined to test paystackapi customer list."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/customer"),
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Customer.list(perPage=50, page=6)
        self.assertEqual(response['status'], True)

    @httpretty.activate
    def test_update(self):
        """Method defined to test paystackapi customer update."""
        httpretty.register_uri(
            httpretty.PUT,
            self.endpoint_url("/customer/4013"),
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Customer.update(customer_id=4013, first_name='andela')
        self.assertEqual(response['status'], True)
