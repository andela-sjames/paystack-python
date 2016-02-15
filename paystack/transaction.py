"""Script used to define the paystack transaction class."""


import requests

from paystack.constants import *


class Transaction(object):
    """docstring for Customer."""

    @staticmethod
    def initialize(reference, amount, email, plan):
        """
        Function defined to create customer.

        first_name: customer's first name.
        last_name: customer's last name.
        email: customer's email address.
        phone;customer's phone number.

        returns: json data from paystack API.
        """
        response = requests.post(
            api_url + 'transaction/initialze',
            data={"reference": reference,
                  "amount": amount,
                  "email": email,
                  "plan": plan
                  }, headers=HEADERS,)

        return response.json()

    @staticmethod
    def charge(authorization_code, email, amount):
        """
        Static method defined to customers by id.

        id: paystack customer id.
        returns: json data from paystack API.
        """
        response = requests.get(
            api_url + 'transaction/charge_authorization',
            data={"authorization_code": authorization_code,
                  "email": email,
                  "amount": amount},
            headers=HEADERS)
        return response.json()

    @staticmethod
    def get(id):
        """
        Static method defined to customers by id.

        id: paystack customer id.
        returns: json data from paystack API.
        """
        response = requests.get(
            api_url + 'transaction/{}' .format(id),
            headers=HEADERS)
        return response.json()

    @staticmethod
    def list():
        """
        Static method defined to list paystack customers.

        args: No argument required.
        returns: json data from paystack API.
        """
        response = requests.get(api_url + 'transaction', headers=HEADERS)
        return response.json()

    @staticmethod
    def totals(self):
        response = requests.get(
            api_url + 'transaction/totals', headers=HEADERS)
        return response.json()

    @staticmethod
    def verify(reference):
        response = requests.get(
            api_url + 'transaction/verify/{}' .format(reference),
            headers=HEADERS)
        return response.json()
