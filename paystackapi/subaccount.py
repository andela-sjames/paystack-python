"""Script used to define the paystack Subaccount class."""

from paystackapi.base import PayStackBase


class SubAccount(PayStackBase):
    """docstring for SubAccount."""

    @classmethod
    def create(cls, **kwargs):
        """
        Function defined to create subaccount.

        Args:
            business_name: name of business for subaccount
            settlement_bank: name of Bank (accepted banks)
            account_number: NUBAN Bank Account number
            percentage_charge: default percentage charged on subaccount?
            **kwargs

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('subaccount', data=kwargs,)

    @classmethod
	def list(cls, **kwargs):
		"""
		List subaccounts
		
		Args:
			perPage: records you want to retrieve per page (Integer)
			page: what page you want to retrieve (Integer)
		
		Returns:
		JSON data from paystack's API.
		"""
		
		return cls().requests.get('subaccount', data=kwargs)
