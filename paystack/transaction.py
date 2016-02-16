"""Script used to define the paystack transaction class."""

import requests

from paystack.constants import *


class Transaction(object):
    """docstring for Transaction."""

    @staticmethod
    def initialize(reference, amount, email, plan):
        """
        Initialize transaction.

        :param reference: unique transaction reference
        :param amount: amount
        :param email: email address
        :param plan: specified plan

        :return: json data from paystack API.
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

        :param reference: Unique transaction reference
        :param authorization_code: Authorization code for the transaction
        :param email: Email Address of the user with the authorization code
        :param amount: Amount in kobo

        :return: json data from paystack API.
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
        Charge token

        :param reference: unique transaction reference
        :param token: paystack token
        :param email: Email Address
        :param amount: Amount in Kobo

        :return: json data from paystack API.
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
        Get a single transaction

        :param id: Transaction id

        :return: json data from paystack API.
        """
        response = requests.get(
            api_url + 'transaction/{}'.format(id),
            headers=HEADERS)
        return response.json()

    @staticmethod
    def list():
        """
        List transactions

        args: No argument required.

        :return: json data from paystack API.
        """
        response = requests.get(api_url + 'transaction', headers=HEADERS)
        return response.json()

    @staticmethod
    def totals():
        """
        Get totals

        :return: json data from paystack API.
        """
        response = requests.get(
            api_url + 'transaction/totals', headers=HEADERS)
        return response.json()

    @staticmethod
    def verify(reference):
        """
        Verify transactions

        :param reference:

        :return: json data from paystack API.
        """
        response = requests.get(
            api_url + 'transaction/verify/{}'.format(reference),
            headers=HEADERS)
        return response.json()
