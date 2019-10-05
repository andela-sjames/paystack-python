import httpretty

from paystackapi.tests.base_test_case import BaseTestCase
from paystackapi.refund import Refund


class TestRefund(BaseTestCase):

	@httpretty.activate
	def test_valid_create(self):
		"""Test Refund Create."""
		httpretty.register_uri(
			httpretty.POST,
			self.endpoint_url("refund"),
			content_type='text/json',
			body='{"status": true, "message": "Refund has been queued for processing", "data": {"transaction": {}, "currency": "NGN", "amount": 180000, "status": "pending"}}',
			status=200,
		)

		response = Refund.create(transaction=1234)
		self.assertTrue(response['status'])
		self.assertIn('message', response)
		self.assertIn('data', response)
		self.assertIn('transaction', response['data'])
		self.assertIn('currency', response['data'])
		

	@httpretty.activate
	def test_list(self):
		"""Test Refund List Method"""
		httpretty.register_uri(
			httpretty.GET,
			self.endpoint_url("refund"),
			content_type='text/json',
			body='{"status": true, "message": "Refunds retrieved", "data": [], "meta": {}}',
			status=200,
		)

		response = Refund.list()
		self.assertTrue(response['status'])
		self.assertIn('message', response)
		self.assertIn('data', response)
		self.assertIn('meta', response)
		self.assertListEqual([], response['data'])
		self.assertDictEqual({}, response['meta'])

	@httpretty.activate
	def test_fetch(self):
		"""Test Refund Fetching"""
		httpretty.register_uri(
			httpretty.GET,
			self.endpoint_url("refund/1234"),
			content_type='text/json',
			body='{"status": true, "message": "Refund retrieved", "data": {"id": 1234}}',
			status=200,
		)

		response = Refund.fetch(refund_id=1234)
		self.assertTrue(response['status'])
		self.assertIn('message', response)
		self.assertIn('data', response)
		self.assertEqual(1234, response['data']['id'])
