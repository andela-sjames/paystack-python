"""Script used to define the paystack Plan class."""
from paystackapi.base import PayStackBase



class TransactionSplit(PayStackBase):
    """docstring for Transaction Split."""

    @classmethod
    def create(cls, **kwargs):
        """
        Create a split payment on your integration

        Args:
            name: Name of the transaction split
            type: The type of transaction split you want to create [ percentage | flat ]
            currency: Any of NGN, GHS, ZAR, or USD
            subaccounts: A list of object containing subaccount code and number of shares
            bearer_type: Any of subaccount | account | all-proportional | all
            bearer_subaccount: Subaccount code
            **kwargs

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('split', data=kwargs)

    @classmethod
    def list(cls, **kwargs):
        """
        List/search for the transaction splits available on your integration.

        Args:
            perPage: records you want to retrieve per page (Integer)
            page: what page you want to retrieve (Integer)

        Returns:
        JSON data from paystack's API.
        """
        return cls().requests.get("split", qs=kwargs)

    @classmethod
    def fetch(cls, split_id):
        """
        Get details of a split on your integration.

        Args:
            split_id: split ID

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get(f"split/{split_id}")

    @classmethod
    def update(cls, split_id, **kwargs):
        """
        Update a transaction split details on your integration

        Args:
            split_id: split ID
            name: Name of the transaction split
            active: True or False
            subaccounts: A list of object containing subaccount code and number of shares
            bearer_type: Any of subaccount | account | all-proportional | all
            bearer_subaccount: Subaccount code
            **kwargs

        Returns:
            Json data from paystack API.
        """
        return cls().requests.put(f"split/{split_id}", data=kwargs)

    @classmethod
    def add_or_update_split_subaccount(cls, split_id, **kwargs):
        """
        Add a Subaccount to a Transaction Split, or update the share of an existing Subaccount in a Transaction Split

        Args:
            split_id: split ID
            subaccount: This is the sub account code
            share: This is the transaction share for the subaccount

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post(f"split/{split_id}/subaccount/add", data=kwargs)

    @classmethod
    def remove_split_subaccount(cls, split_id, **kwargs):
        """
        Remove a subaccount from a transaction split

        Args:
            split_id: split ID
            subaccount: This is the sub account code

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post(f"split/{split_id}/subaccount/remove", data=kwargs)
