"""Base script used across defined."""

import requests
from constants import API_URL


class Borg:
    """Borg class making class attributes global"""
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class PayStackBase(Borg):
    """Base Class used across defined."""

    def __init__(self, **kwargs):
        """Initialize Paystack with secret key."""
        Borg.__init__(self)
        arguments = dict(api_url=API_URL)
        if kwargs.get('secret_key', None):
            arguments['headers'] = {
                'Authorization': 'Bearer {secret_key}'.format(**kwargs)
            }
            req = PayStackRequests(**arguments)
            self._shared_state.update(requests=req)
        self._shared_state.update(kwargs)


class PayStackRequests(object):

    def __init__(self, api_url='https://api.paystack.co/',
                 headers=None):
        """Initialize Paystack Request object for browsing resource.

        Args:
            api_url: str
            headers: dict
        """
        self.API_BASE_URL = '{api_url}'.format(**locals())
        self.headers = headers

    def _request(self, method, resource_uri, **kwargs):
        """Perform a method on a resource.

        Args:
            method: requests.`method`
            resource_uri: resource endpoint
        Raises:
            HTTPError
        Returns:
            JSON Response
        """
        response = method(self.API_BASE_URL + resource_uri,
                          data=kwargs, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get(self, endpoint, **kwargs):
        """Get a resource.

        Args:
            endpoint: resource endpoint.
        """
        return self._request(requests.get, endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        """Create a resource.

        Args:
            endpoint: resource endpoint.
        """
        return self._request(requests.post, endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        """Update a resource.

        Args:
            endpoint: resource endpoint.
        """
        return self._request(requests.put, endpoint, **kwargs)
