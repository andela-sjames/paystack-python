"""Script used to define the paystack Miscellaneous class."""

from paystackapi.base import PayStackBase


class Misc(PayStackBase):
	
	@classmethod
	def list_banks(cls):
		"""Static method defined to list banks.
			Args:
				No argument required.
			Returns:
				Json data from paystack API.
		"""
		return cls().requests.get('bank')
