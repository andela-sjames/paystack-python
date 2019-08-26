"""Script used to define the paystack Plan class."""

from paystackapi.base import PayStackBase


class Plan(PayStackBase):
    """docstring for Plan."""

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
        return cls().requests.post('plan', data=kwargs)

    @classmethod
    def get(cls, plan_id):
        """
        Get a single plan.

        Args:
            plan_id: paystack plan id.

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get(f"plan/{plan_id}")

    @classmethod
    def list(cls):
        """
        Static method defined to list paystack plan.

        Args:
            No argument required.
        Returns:
            Json data from paystack API.
        """
        return cls().requests.get('plan')

    @classmethod
    def update(cls, plan_id, **kwargs):
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
        return cls().requests.put(f"plan/{plan_id}", data=kwargs,)
