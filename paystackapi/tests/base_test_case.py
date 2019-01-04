import unittest


class BaseTestCase(unittest.TestCase):
		
	def endpoint_url(self, path):
		if path[0] == '/':
			return 'https://api.paystack.co{}'.format(path)
		return 'https://api.paystack.co/{}'.format(path)
