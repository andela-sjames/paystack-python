"""Script used to define the paystack transaction class."""


import requests

from paystack.constants import *


class Transaction(object):
    """docstring for Transaction."""

    @staticmethod
    def initialize(reference, amount, email, plan):
        """
        Initialize transaction.

        Args:
            reference: unique transaction reference
            amount: amount
            email: email address
            plan: specified plan

        Returns:
            Json data from paystack API.
        """
        response = requests.post(
            api_url + 'transaction/initialize',
            data={"reference": reference,
                  "amount": amount,
                  "email": email,
                  "plan": plan
                  }, headers=HEADERS, )

        return response.json()

    @staticmethod
    def charge(reference, authorization_code, email, amount):
        """
        Charge authorization.

        Args:
            reference: Unique transaction reference
            authorization_code: Authorization code for the transaction
            email: Email Address of the user with the authorization code
            amount: Amount in kobo

        Returns:
            Json data from paystack API.
        """
        response = requests.post(
            api_url + 'transaction/charge_authorization',
            data={"reference": reference,
                  "authorization_code": authorization_code,
                  "email": email,
                  "amount": amount},
            headers=HEADERS)

        return response.json()

    @staticmethod
    def charge_token(reference, token, email, amount):
        """
        Charge token.

        Args:
            reference: unique transaction reference
            token: paystack token
            email: Email Address
            amount: Amount in Kobo

        Returns:
            Json data from paystack API.
        """
        response = requests.post(
            api_url + 'transaction/charge_token',
            data={"reference": reference,
                  "token": token,
                  "email": email,
                  "amount": amount
                  },
            headers=HEADERS)
        return response.json()

    @staticmethod
    def get(id):
        """
        Get a single transaction.

        Args:
            id: Transaction id(integer).

        Returns:
            Json data from paystack API.
        """
        response = requests.get(
            api_url + 'transaction/{}'.format(id),
            headers=HEADERS)
        return response.json()

    @staticmethod
    def list():
        """
        List transactions

        Args:
            No argument required.

        Returns:
            Json data from paystack API.
        """
        response = requests.get(api_url + 'transaction', headers=HEADERS)
        return response.json()

    @staticmethod
    def totals():
        """
        Get totals.

        Args:
            No argument required.

        Returns:
            Json data from paystack API.
        """
        response = requests.get(
            api_url + 'transaction/totals', headers=HEADERS)
        return response.json()

    @staticmethod
    def verify(reference):
        """
        Verify transactions

        Args:
            reference: a unique value needed for transaction.

        Returns:
            Json data from paystack API.
        """
        response = requests.get(
            api_url + 'transaction/verify/{}'.format(reference),
            headers=HEADERS)
        return response.json()
