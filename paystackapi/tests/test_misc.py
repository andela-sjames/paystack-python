import httpretty

from paystackapi.misc import Misc
from paystackapi.tests.base_test_case import BaseTestCase


class TestMisc(BaseTestCase):
	
	@httpretty.activate
	def test_list_banks(self):
		httpretty.register_uri(
			httpretty.GET,
			self.endpoint_url("/bank"),
			content_type='text/json',
			body='{"status": true, "message": "Banks retrieved", "data": []}',
			status=200,
		)
		
		response = Misc.list_banks()
		self.assertTrue(response['status'])
		self.assertListEqual([], response['data'])
