"""Base script used across defined."""

import requests


class PayStackBase(object):
    """Base Class used across defined."""

    @classmethod
    def __init__(cls, paystack_secret_key=None):
        """Initialize Paystack with secret key."""
        cls.secret_key = paystack_secret_key
        PayStackBase.headers = {'Authorization': 'Bearer ' + cls.secret_key}


class PayStackRequests(object):

    def __init__(self, API_URL, HEADERS):
        self.API_URL = '{API_URL}'.format(locals())
        self.headers = HEADERS

    def get(self, endpoint, **kwargs):
        resource_uri = '{API_URL}/{endpoint}'.format(locals())
        return requests.get(resource_uri, data=kwargs,
                            headers=self.HEADERS)

    def post(self, endpoint, **kwargs):
        resource_uri = '{API_URL}/{endpoint}'.format(locals())
        return requests.post(resource_uri, data=kwargs,
                             headers=self.HEADERS)

    def put(self, endpoint, **kwargs):
        resource_uri = '{API_URL}/{endpoint}'.format(locals())
        return requests.post(resource_uri, data=kwargs,
                             headers=self.HEADERS)
