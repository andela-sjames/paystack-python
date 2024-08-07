"""Script used to define Paystack subscription class"""

from paystackapi.base import PayStackBase


class Subscription(PayStackBase):
    """docstring for Subscription."""

    @classmethod
    def create(cls, **kwargs):
        """
        Create subscription.

        Args:
            customer: Customer's email address or customer code
            plan: Plan code
            authorization: customers authorization code
            start_date:  the date for the first debit. (ISO 8601 format)

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('subscription', data=kwargs)

    @classmethod
    def list(cls, **kwargs):
        """
        List subscriptions.

        Optional Args:
            perPage: Number of subscriptions listed per page for pagination
            page: pagination page number.
            customer: Customer ID.
            plan: Plan ID.

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get('subscription', qs=kwargs)

    @classmethod
    def disable(cls, **kwargs):
        """
        Disables subscription
        Args:
            code: Subscription code
            token: Email token
        returns:
            Json data from paystack API
        """
        return cls().requests.post('subscription/disable', data=kwargs)

    @classmethod
    def enable(cls, **kwargs):
        """
        Disables subscription

        Args:
            code: Subscription code
            token: Email token

        returns:
            Json data from paystack API
        """
        return cls().requests.post('subscription/enable', data=kwargs)

    @classmethod
    def fetch(cls, subscription_id):
        """
        Fetch subscription.

        Args:
            subscription_id: subscription id.

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get(f"subscription/{subscription_id}")

    @classmethod
    def generate_update_subscription_link(cls, subscription_code):
        """
        Generate a link for updating the card on a subscription
        
        Args:
            subscription_code: subscription code.
        
        Returns:
            Json data from paystack API.
        """
        return cls().requests.get(f"subscription/{subscription_code}/manage/link")
    
    @classmethod
    def send_update_subscription_link(cls, subscription_code):
        """
        Email a customer a link for updating the card on their subscription
        
        Args:
            subscription_code: subscription code.
        
        Returns:
            Json data from paystack API.
        """
        return cls().requests.post(f"subscription/{subscription_code}/manage/email")