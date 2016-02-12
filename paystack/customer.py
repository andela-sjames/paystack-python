"""Script used to define the customer class."""


import requests

PAY_SECRET_KEY = 'sk_test_0a246ef179dc841f42d20959bebdd790f69605d8'
HEADERS = {'Authorization': 'Bearer ' + PAY_SECRET_KEY}
api_url = 'https://api.paystack.co/'


class Customer(object):
    """docstring for ClassName."""

    @staticmethod
    def create(first_name, last_name, email, phone):
        """
        Function defined to create customer.

        first_name: customer's first name.
        last_name: customer's last name.
        email: customer's email address.
        phone;customer's phone number.

        returns: json data from paystack API.
        """
        response = requests.post(
            api_url + 'customer',
            data={"first_name": first_name,
                  "last_name": last_name,
                  "email": email,
                  "phone": phone
                  }, headers=HEADERS,)

        return response.json()

    @staticmethod
    def get(id):
        """
        Static method defined to customers by id.

        id: paystack customer id.
        returns: json data from paystack API.
        """
        response = requests.get(
            api_url + 'customer/{}' .format(id),
            headers=HEADERS)
        return response.json()

    @staticmethod
    def list():
        """
        Static method defined to list paystack customers.

        args: No argument required.
        returns: json data from paystack API.
        """
        response = requests.get(api_url + 'customer', headers=HEADERS)
        return response.json()

    @staticmethod
    def update(id, first_name=None, last_name=None, email=None, phone=None):
        """
        Static method defined to update paystack customer data by id.

        id: paystack customer id.
        first_name: customer's first name.
        last_name: customer's last name.
        email: customer's email address.
        phone;customer's phone number.

        returns: json data from paystack API.
        """
        response = requests.put(
            api_url + 'customer/{}' .format(id),
            data={"first_name": first_name,
                  "last_name": last_name,
                  "email": email,
                  "phone": phone
                  }, headers=HEADERS)
        return response.json()
