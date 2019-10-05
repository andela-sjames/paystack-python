from paystackapi.base import PayStackBase


class Refund(PayStackBase):
	
	@classmethod
	def create(cls, **kwargs):
		"""
		Function defined to create a refund.

		Args:
		transaction: Transaction reference or id
		amount: How much in kobo to be refunded to the customer - Optional
		currency: Three-letter ISO currency - Optional
		customer_note: Customer reason - Optional
		merchant_note: Merchant reason - Optional
		
		Returns:
		Json data from paystack API.
		"""
		
		return cls().requests.post('refund', data=kwargs)
	
	@classmethod
	def list(cls, **kwargs):
		"""
		List Refunds
		
		Args:
			reference: Identifier for transaction to be refunded - Optional
			currency: Three-letter ISO currency - Optional
		
		Returns:
		JSON data from paystack's API.
		"""
		
		return cls().requests.get('refund', data=kwargs)
	
	@classmethod
	def fetch(cls, refund_id):
		"""
		Fetch a Refund
		
		Args:
			refund_id: Identifier for refund to be fetched
		
		Return:
			JSON data from paystack API
		"""
		
		return cls().requests.get(f"refund/{refund_id}")
