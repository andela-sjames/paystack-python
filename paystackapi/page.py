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

    @classmethod
    def list(cls, perPage, page):
        """
        List pages
        
        Args:
            perPage: records you want to retrieve per page (Integer)
            page: what page you want to retrieve (Integer)
        
        Returns:
        JSON data from paystack's API.
        """
        return cls().requests.get(f"page?perPage={perPage}&page={page}")

