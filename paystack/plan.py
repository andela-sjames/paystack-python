import requests

# from paystack.constants import *

PAYSTACK_SECRET_KEY = 'sk_test_2de5b5dc4d578f5e431b67b061f48925f44fb2f1'
HEADERS = {'Authorization': 'Bearer ' + PAYSTACK_SECRET_KEY}
api_url = 'https://api.paystack.co/'


class Plan(object):
    """docstring for Customer."""

    @staticmethod
    def create(name, description, amount, interval, send_invoices, send_sms, hosted_page, hosted_page_url, hosted_page_summary, currency):

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
                  }, headers=HEADERS,)

        return response.json()

    @staticmethod
    def get(id):
        response = requests.get(
            api_url + 'plan/{}' .format(id),
            headers=HEADERS)
        return response.json()

    @staticmethod
    def list():
        response = requests.get(
            api_url + 'plan/',
            headers=HEADERS)
        return response.json()

    @staticmethod
    def update(id, name=None, description=None, amount=None, interval=None, send_invoices=None, send_sms=None, hosted_page=None, hosted_page_url=None, hosted_page_summary=None, currency=None):
        response = requests.put(
            api_url + 'plan/{}' .format(id),
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



# print Plan.create("Noibi Kazeem", "The chronic debtor", 50000, 'daily', True, True, 'url', 'url', 'details', 'NGN')

# print Transaction.totals()
# print Transaction.list()
# print Transaction.initialize('aCp88HQhks', 35000, 'jubrilissa@gmail.com')

# print Transaction.verify('aCp88HQhgw')

# 18084633536.63683

# print Transaction.charge('aCp88HQhk43', 'AUTH_zcoidxl6', 'oreoluwa@gmail.com', 35000)
#
# print Transaction.charge_token()

print Plan.update(78, interval="monthly", amount=70000)
