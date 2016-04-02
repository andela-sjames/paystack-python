"""Base script used across defined."""

import requests
from constants import API_URL


class PayStackBase(object):
    """Base Class used across defined."""

    def __init__(self, secret_key=None):
        """Initialize Paystack with secret key."""
        self.requests = PayStackRequests(
            api_url=API_URL,
            headers={'Authorization': 'Bearer {}'.format(secret_key)}
        )


class PayStackRequests(object):

    def __init__(self, api_url='http://https://api.paystack.co/',
                 headers=None):
        self.API_URL = '{api_url}'.format(**locals())
        self.headers = headers

    def get(self, endpoint, **kwargs):
        resource_uri = '{api_url}/{endpoint}'.format(**locals())
        return requests.get(resource_uri, data=kwargs,
                            headers=self.headers)

    def post(self, endpoint, **kwargs):
        resource_uri = '{api_url}/{endpoint}'.format(**locals())
        return requests.post(resource_uri, data=kwargs,
                             headers=self.headers)

    def put(self, endpoint, **kwargs):
        resource_uri = '{api_url}/{endpoint}'.format(**locals())
        return requests.post(resource_uri, data=kwargs,
                             headers=self.headers)
