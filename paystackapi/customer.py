"""Script used to define the paystack Customer class."""

from paystackapi.base import PayStackBase


class Customer(PayStackBase):
    """docstring for Customer."""

    @classmethod
    def create(cls, **kwargs):
        """
        Function defined to create customer.

        Args:
            first_name: customer's first name.
            last_name: customer's last name.
            email: customer's email address.
            phone:customer's phone number.

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('customer', data=kwargs,)

    @classmethod
    def get(cls, customer_id):
        """
        Static method defined to get customers by id.

        Args:
            customer_id: paystack customer id.
        Returns:
            Json data from paystack API.
        """
        return cls().requests.get(f"customer/{customer_id}")

    @classmethod
    def list(cls):
        """
        Static method defined to list paystack customers.

        Args:
            No argument required.
        Returns:
            Json data from paystack API.
        """
        return cls().requests.get('customer')

    @classmethod
    def update(cls, customer_id, **kwargs):
        """
        Static method defined to update paystack customer data by id.

        Args:
            customer_id: paystack customer id.
            first_name: customer's first name(optional).
            last_name: customer's last name(optional).
            email: customer's email address(optional).
            phone:customer's phone number(optional).

        Returns:
            Json data from paystack API.
        """
        return cls().requests.put(f"customer/{customer_id}", data=kwargs,)
