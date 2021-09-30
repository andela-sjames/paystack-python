"""Script defined to test the Customer class."""

import httpretty

from paystackapi.transaction_split import TransactionSplit
from paystackapi.tests.base_test_case import BaseTestCase


class TestTransactionSplit(BaseTestCase):
    """Method defined to test transaction split initialize."""

    @httpretty.activate
    def test_transaction_split_create(self):
        """Method defined to test transaction split create."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("split"),
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = TransactionSplit.create(
            name='somes', type=12000, 
            currency='NGN', bearer_type='account'
        )
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_transaction_split_list(self):
        """Method defined to test transaction split list."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("split"),
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = TransactionSplit.list()
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_transaction_split_fetch(self):
        """Method defined to test transaction split fetch."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/split/1445"),
            content_type='text/json',
            body='{"status": true, "message": "Transaction Split Subaccount retrieved"}',
            status=201,
        )

        response = TransactionSplit.fetch(split_id='1445')
        self.assertEqual(response['status'], True)
    
    @httpretty.activate
    def test_transaction_split_update(self):
        """Method defined to test transaction split update."""
        httpretty.register_uri(
            httpretty.PUT,
            self.endpoint_url("/split/1445"),
            content_type='text/json',
            body='{"status": true, "message": "Transaction Split updated"}',
            status=201,
        )

        response = TransactionSplit.update(split_id='1445')
        self.assertEqual(response['status'], True)

    @httpretty.activate
    def test_transaction_split_add_or_update_split_subaccount(self):
        """Method defined to test transaction split add_or_update_split_subaccount."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("split/1445/subaccount/add"),
            content_type='text/json',
            body='{"status": true, "message": "Transaction Split Subaccount Updated"}',
            status=201,
        )

        response = TransactionSplit.add_or_update_split_subaccount(split_id='1445')
        self.assertEqual(response['status'], True)
    
    @httpretty.activate
    def test_transaction_split_remove_split_subaccount(self):
        """Method defined to test transaction split remove_split_subaccount."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("split/1445/subaccount/remove"),
            content_type='text/json',
            body='{"status": true, "message": "Transaction Split Subaccount Removed"}',
            status=201,
        )

        response = TransactionSplit.remove_split_subaccount(split_id='1445')
        self.assertEqual(response['status'], True)