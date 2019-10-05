"""Script used to define the paystack Page class."""

from paystackapi.base import PayStackBase


class Page(PayStackBase):
    """docstring for Page."""

    @classmethod
    def create(cls, **kwargs):
        """
        method defined to create a new page.

        Args:
            name: name of page
            **kwargs

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('page', data=kwargs,)

    @classmethod
    def list(cls, **kwargs):
        """
        List pages
        
        Args:
            perPage: records you want to retrieve per page (Integer)
            page: what page you want to retrieve (Integer)
        
        Returns:
        JSON data from paystack's API.
        """
        return cls().requests.get("page", qs=kwargs)

    @classmethod
    def fetch(cls, id_or_slug):
        """
        Get a single page by id or slug.

        Args:
            id_or_slug: id or slug

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get(f"page/{id_or_slug}")

    @classmethod
    def update(cls, id_or_slug, **kwargs):
        """
        Update a single page by id or slug.

        Args:
            id_or_slug: id or slug
            **kwargs

        Returns:
            Json data from paystack API.
        """
        return cls().requests.put(f"page/{id_or_slug}", data=kwargs,)

    @classmethod
    def is_slug_available(cls, slug):
        """
        Check if a slug is available.

        Args:
            slug: URL slug to be confirmed

        Returns:
            Json data from paystack API.
        """
        return cls().requests.put(f"page/check_slug_availability/{slug}")

    @classmethod
    def add_products(cls, payment_page_id, **kwargs):
        """
        Add products to page

        Args:
            payment_page_id: Id of the payment page (Integer)
            product: Ids of all the products i.e. [473, 292]

        Returns:
            Json data from paystack API.
        """
        return cls().requests.put(f"page/{payment_page_id}/product", data=kwargs,)
