"""Script used to define the paystack Product class."""

from paystackapi.base import PayStackBase


class Product(PayStackBase):
    """docstring for Product."""

    @classmethod
    def create(cls, **kwargs):
        """
        Function defined to create product.

        Args:
            name: name of the product
            description: description of product
            price: price of the product, in kobo(Integer)
            currency: currency in which amount should be charged
            **kwargs

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('product', data=kwargs,)

    @classmethod
    def list(cls):
        """
        List Products.

        Args:
            No argument required.

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get('product')

    @classmethod
    def fetch(cls, product_id):
        """
        Get a single product by id.

        Args:
            product_id: Product id(integer).

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get(f"product/{product_id}")

    @classmethod
    def update(cls, product_id, **kwargs):
        """
        Static method defined to update product by id.

        Args:
            product_id: paystack product id.
            name: name of the product
            description: description of product
            price: price of the product, in kobo(Integer)
            currency: currency in which amount should be charged
            **kwargs

        Returns:
            Json data from paystack API.
        """
        return cls().requests.put(f"product/{product_id}", data=kwargs,)
