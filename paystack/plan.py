"""Script used to define the paystack Plan class."""


import requests

from paystack.constants import *


class Plan(object):
    """docstring for Plan."""

    @staticmethod
    def create(name, description, amount, interval, send_invoices, send_sms,
               hosted_page, hosted_page_url,
               hosted_page_summary, currency):
        """
        Function defined to create a plan.

        Args:
            name: plan's name.
            description: description of the plan.
            amount: amount for the plan
            interval: plan's interval
            send_invoices: boolean
            send_sms:
            hosted_page:
            hosted_page_url: url of hosted page
            hosted_page_summary: summary of the hosted page
            currency: plans currency

        Returns:
            Json data from paystack API.
        """
        response = requests.post(
            api_url + 'plan',
            data={"name": name,
                  "description": description,
                  "amount": amount,
                  "interval": interval,
                  "send_invoices": send_invoices,
                  "send_sms": send_sms,
                  "hosted_page": hosted_page,
                  "hosted_page_url": hosted_page_url,
                  "hosted_page_summary": hosted_page_summary,
                  "currency": currency
                  }, headers=HEADERS, )

        return response.json()

    @staticmethod
    def get(id):
        """
        Get a single plan.

        Args:
            id: paystack plan id.

        Returns:
            Json data from paystack API.
        """
        response = requests.get(
            api_url + 'plan/{}'.format(id),
            headers=HEADERS)
        return response.json()

    @staticmethod
    def list():
        """
        Static method defined to list paystack plan.

        Args:
            No argument required.
        Returns:
            Json data from paystack API.
        """
        response = requests.get(
            api_url + 'plan/',
            headers=HEADERS)
        return response.json()

    @staticmethod
    def update(id, name=None, description=None, amount=None, interval=None,
               send_invoices=None, send_sms=None,
               hosted_page=None, hosted_page_url=None,
               hosted_page_summary=None, currency=None):
        """
        Static method defined to list paystack plan.

        Args:
            id: plan identity number.
            name: name of plan
            description: plan description(optional)
            amount: plan amount in Naira
            interval: plan interval
            send_invoice:
            send_sms: (optional)
            hosted_page: (optional)
            hosted_page_url: (optional)
            hosted_page_summary: (optional)
            currency: Naira
        Returns:
            Json data from paystack API.
        """
        response = requests.put(
            api_url + 'plan/{}'.format(id),
            data={"name": name,
                  "description": description,
                  "amount": amount,
                  "interval": interval,
                  "send_invoices": send_invoices,
                  "send_sms": send_sms,
                  "hosted_page": hosted_page,
                  "hosted_page_url": hosted_page_url,
                  "hosted_page_summary": hosted_page_summary,
                  "currency": currency

                  },
            headers=HEADERS
        )
        return response.json()
