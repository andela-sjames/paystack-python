"""Script used to define the paystack settlement class."""

from paystackapi.base import PayStackBase


class Settlement(PayStackBase):
    """docstring for settlement."""

    @classmethod
    def fetch(cls, start_date, end_date, subaccount):
        """
        Function defined to fetch settlement.

        Args:
            start_date: Lower bound of date range. 
                  Leave undefined to export settlement from day one.
            end_date: Upper bound of date range. 
                Leave undefined to export settlements till date.
            subaccount: code to export only settlements for that subaccount. 
                        Set to none to export only transactions for the account.

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get(f"settlement?from={start_date}&to={end_date}&subaccount={subaccount}")
