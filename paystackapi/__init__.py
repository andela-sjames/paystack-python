import os

"""Script used to define constants used across codebase."""

SECRET_KEY = os.getenv(
    'PAYSTACK_SECRET_KEY',
    'sk_test_0a246ef179dc841f42d20959bebdd790f69605d8')
HEADERS = {'Authorization': 'Bearer {}'}
API_URL = 'https://api.paystack.co/'
