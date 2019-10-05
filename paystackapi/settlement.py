"""Script used to define the paystack settlement class."""

from paystackapi.base import PayStackBase


class Settlement(PayStackBase):
    """docstring for settlement."""

    @classmethod
    def fetch(cls, **kwargs):
        """
        Function defined to fetch settlement.

        Args:
            from: Lower bound of date range. 
                  Leave undefined to export settlement from day one.
            to: Upper bound of date range. 
                Leave undefined to export settlements till date.
            subaccount: code to export only settlements for that subaccount. 
                        Set to none to export only transactions for the account.

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get("settlement", qs=kwargs)
