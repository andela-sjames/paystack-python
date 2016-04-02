"""Script used to define the paystack Plan class."""

from paystackapi.constants import HEADERS, API_URL
from paystackapi.base import PayStackBase, PayStackRequests


class Plan(PayStackBase):
    """docstring for Plan."""

    def __init__(self):
        self.requests = PayStackRequests(api_url=API_URL,
                                         headers=HEADERS)

    @classmethod
    def create(cls, **kwargs):
        """
        Function defined to create a plan.

        Args:
            name: plan's name.
            description: description of the plan.
            amount: amount for the plan in kobo
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
        cls.headers = None
        response = cls().requests.post('plan', data=kwargs)

        return response.json()

    @classmethod
    def get(cls, plan_id):
        """
        Get a single plan.

        Args:
            plan_id: paystack plan id.

        Returns:
            Json data from paystack API.
        """
        response = cls().requests.get('plan/{plan_id}'.format(locals()))
        return response.json()

    @classmethod
    def list(cls):
        """
        Static method defined to list paystack plan.

        Args:
            No argument required.
        Returns:
            Json data from paystack API.
        """
        response = cls().requests.get('plan')
        return response.json()

    @classmethod
    def update(cls, id, **kwargs):
        """
        Static method defined to update paystack plan.

        Args:
            plan_id: plan identity number.
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
        cls.headers = None
        response = cls().requests.put('plan/{plan_id}'.format(locals()),
                                      data=kwargs)
        return response.json()
