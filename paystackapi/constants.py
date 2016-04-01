"""Script used to define constants used accross codebase."""

PAYSTACK_SECRET_KEY = 'sk_test_0a246ef179dc841f42d20959bebdd790f69605d8'
HEADERS = {'Authorization': 'Bearer ' + PAYSTACK_SECRET_KEY}
api_url = 'https://api.paystack.co/'


class Paystack(object):
    """Classs used to instantiate paystack."""

    def __init__(self, PAYSTACK_SECRET_KEY=None):
        self.paystack_secret = PAYSTACK_SECRET_KEY
        pass
