"""Script used to define the paystack Customer class."""


import requests

from paystackapi.constants import *


class Customer(object):
    """docstring for Customer."""

    @classmethod
    def create(cls, first_name, last_name, email, phone):
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
        response = requests.post(
            api_url + 'customer',
            data={"first_name": first_name,
                  "last_name": last_name,
                  "email": email,
                  "phone": phone
                  }, headers=HEADERS,)

        return response.json()

    @classmethod
    def get(cls, id):
        """
        Static method defined to get customers by id.

        Args:
            id: paystack customer id.
        Returns:
            Json data from paystack API.
        """
        response = requests.get(
            api_url + 'customer/{}' .format(id),
            headers=HEADERS)
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
        response = requests.get(api_url + 'customer', headers=HEADERS)
        return response.json()

    @classmethod
    def update(cls, id, first_name=None, last_name=None, email=None, phone=None):
        """
        Static method defined to update paystack customer data by id.

        Args:
            id: paystack customer id.
            first_name: customer's first name(optional).
            last_name: customer's last name(optional).
            email: customer's email address(optional).
            phone:customer's phone number(optional).

        Returns:
            Json data from paystack API.
        """
        response = requests.put(
            api_url + 'customer/{}' .format(id),
            data={"first_name": first_name,
                  "last_name": last_name,
                  "email": email,
                  "phone": phone
                  }, headers=HEADERS)
        return response.json()
