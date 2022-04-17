"""Script used to define the paystack Miscellaneous class."""

from paystackapi.base import PayStackBase


class Misc(PayStackBase):
	
	@classmethod
	def list_banks(cls, **kwargs):
		"""
			Static method defined to list banks.
			
			Args:
				No argument is required.

				country (str): The country from which to obtain the list of supported banks. e.g country=ghana or country=nigeria
				
				gateway (str): The gateway type of the bank. It can be one of these: [emandate, digitalbankmandate]
				
				currency (str): Any of NGN, USD, GHS or ZAR
			
			Returns:
				Json data from paystack API.
		"""
		return cls().requests.get('bank', qs=kwargs)
