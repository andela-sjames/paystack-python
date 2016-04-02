"""Script used to define the paystack Customer class."""

from paystackapi.constants import HEADERS, API_URL
from paystackapi.base import PayStackBase, PayStackRequests


class Customer(PayStackBase):
    """docstring for Customer."""

    def __init__(self):
        self.requests = PayStackRequests(api_url=API_URL,
                                         headers=HEADERS)

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
        response = cls().requests.post('customer', data=kwargs,)

        return response.json()

    @classmethod
    def get(cls, customer_id):
        """
        Static method defined to get customers by id.

        Args:
            customer_id: paystack customer id.
        Returns:
            Json data from paystack API.
        """
        response = cls().requests.get(
            'customer/{customer_id}'.format(locals()))
        return response.json()

    @classmethod
    def list(cls):
        """
        Static method defined to list paystack customers.

        Args:
            No argument required.
        Returns:
            Json data from paystack API.
        """
        response = cls().requests.get('customer')
        return response.json()

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
        response = cls().requests.put(
            'customer/{customer_id}'.format(locals()),
            data=kwargs)
        return response.json()
