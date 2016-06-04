"""Script defined to test the Plan class."""


import unittest
import httpretty

from paystackapi.plan import Plan


class TestPlan(unittest.TestCase):
    """Class to test Plans."""

    @httpretty.activate
    def test_create(self):
        """Method defined to test plan creation."""
        httpretty.register_uri(
            httpretty.POST,
            "https://api.paystack.co/plan",
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
            "https://api.paystack.co/plan/78",
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
            "https://api.paystack.co/plan",
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
            "https://api.paystack.co/plan/78",
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Plan.update(plan_id=78, interval="monthly", amount=70000)
        self.assertEqual(response['status'], True)
