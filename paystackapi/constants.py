"""Script used to define constants used accross codebase."""

PAYSTACK_SECRET_KEY = 'sk_test_0a246ef179dc841f42d20959bebdd790f69605d8'
HEADERS = {'Authorization': 'Bearer ' + PAYSTACK_SECRET_KEY}
api_url = 'https://api.paystack.co/'


class PayStackBase(object):

    secret_key = ''
    paystack_secret_key = secret_key
    headers = {'Authorization': 'Bearer ' + paystack_secret_key}

    @classmethod
    def __init__(cls, paystack_secret_key=paystack_secret_key):
        PayStackBase.secret_key = paystack_secret_key
