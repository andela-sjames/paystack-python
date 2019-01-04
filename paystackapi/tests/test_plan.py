"""Script defined to test the Plan class."""

import httpretty
from paystackapi.tests.base_test_case import BaseTestCase

from paystackapi.plan import Plan


class TestPlan(BaseTestCase):
    """Class to test Plans."""

    @httpretty.activate
    def test_create(self):
        """Method defined to test plan creation."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/plan"),
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Plan.create(
            name="John Doe", description="Payment plan for awesome people contributions",
            amount=50000, interval="daily", send_invoices=True, )
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_get(self):
        """Function defined to test Plan get method."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/plan/78"),
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Plan.get(plan_id=78)
        self.assertEqual(response['status'], True)

    @httpretty.activate
    def test_list(self):
        """Function defined to test paystackapi plan list method."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/plan"),
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Plan.list()
        self.assertEqual(response['status'], True)

    @httpretty.activate
    def test_update(self):
        """Function defined to test paystackapi plan update."""
        httpretty.register_uri(
            httpretty.PUT,
            self.endpoint_url("/plan/78"),
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Plan.update(plan_id=78, interval="monthly", amount=70000)
        self.assertEqual(response['status'], True)
