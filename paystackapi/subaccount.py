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
        return cls().requests.get("subaccount", qs=kwargs,)

    @classmethod
    def fetch(cls, id_or_slug):
        """
        Get a single subaccount by id or slug.

        Args:
            id_or_slug: id or subaccount_code

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get(f"subaccount/{id_or_slug}")

    @classmethod
    def update(cls, id_or_slug, **kwargs):
        """
        Update a single subaccount by id or slug.

        Args:
            id_or_slug: id or subaccount_code
            business_name: name of business for subaccount
            settlement_bank: name of Bank (accepted banks)
            account_number: NUBAN Bank Account number
            percentage_charge: default percentage charged on subaccount?
            **kwargs

        Returns:
            Json data from paystack API.
        """
        return cls().requests.put(f"subaccount/{id_or_slug}", data=kwargs,)
