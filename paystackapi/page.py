"""Script used to define the paystack Page class."""

from paystackapi.base import PayStackBase


class Page(PayStackBase):
    """docstring for Page."""

    @classmethod
    def create(cls, **kwargs):
        """
        Function defined to create a new page.

        Args:
            name: name of page
            **kwargs

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('page', data=kwargs,)
