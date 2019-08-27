"""Script used to define the paystack Product class."""

from paystackapi.base import PayStackBase


class Product(PayStackBase):
    """docstring for Product."""

    @classmethod
    def create(cls, **kwargs):
        """
        Function defined to create customer.

        Args:
            name: name of the product
            description: description of product
            price: price of the product, in kobo
            currency: customer's phone number.

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('product', data=kwargs,)
