import unittest
import httpretty
from paystackapi.misc import Misc


class TestMisc(unittest.TestCase):
	
	@httpretty.activate
	def test_list_banks(self):
		httpretty.register_uri(
			httpretty.GET,
			"https://api.paystack.co/bank",
			content_type='text/json',
			body='{"status": true, "message": "Banks retrieved", "data": []}',
			status=200,
		)
		
		response = Misc.list_banks()
		self.assertTrue(response['status'])
		self.assertListEqual([], response['data'])
