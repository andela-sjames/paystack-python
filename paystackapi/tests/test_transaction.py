"""Script defined to test the Customer class."""


import unittest

import mock

from paystackapi.transaction import Transaction


class TestTransaction(unittest.TestCase):
    """Method defined to test transaction initialize."""

    def test_initialize(self):
        with mock.patch('paystackapi.transaction.Transaction.initialize') \
                as mock_initialize:
                mock_initialize.return_value = {
                    'status': True, 'message': 'Authorization URL created',
                    'data': {
                        'authorization_url': 'https://standard.paystackapi.co/pay/xam1uq26de',
                        'access_code': 'xam1uq26de',
                        'reference': 'getupall'
                    }
                }

                response = Transaction.initialize(
                    'getupall', 12000,
                    'samuel.james@andela.com',
                    'daily')
                self.assertTrue(response['status'])

    def test_charge(self):
        with mock.patch('paystackapi.transaction.Transaction.charge') as \
                mock_charge:
                mock_charge.return_value = {
                    'status': True
                }

                response = Transaction.charge(
                    'getupall', 'authorization_code'
                    'email', 'amount')
                self.assertTrue(response['status'])

    def test_charge_token(self):
        with mock.patch('paystackapi.transaction.Transaction.charge_token') as \
                mock_charge_token:
                mock_charge_token.return_value = {
                    'status': True
                }

                response = Transaction.charge_token(
                    'getupall', 'token'
                    'email', 'amount')
                self.assertTrue(response['status'])

    def test_get(self):
        with mock.patch('paystackapi.transaction.Transaction.get') as \
                mock_get:
                mock_get.return_value = {
                    'status': True
                }

                response = Transaction.get(4013)
                self.assertTrue(response['status'])

    def test_list(self):
        with mock.patch('paystackapi.transaction.Transaction.list') as \
                mock_list:
                mock_list.return_value = {
                    'status': True
                }

                response = Transaction.list()
                self.assertTrue(response['status'])

    def test_totals(self):
        with mock.patch('paystackapi.transaction.Transaction.totals') as \
                mock_totals:
                mock_totals.return_value = {
                    'status': True
                }

                response = Transaction.totals()
                self.assertTrue(response['status'])

    def test_verify(self):
        with mock.patch('paystackapi.transaction.Transaction.verify') as \
                mock_verify:
                mock_verify.return_value = {
                    'status': True
                }

                response = Transaction.verify('reference')
                self.assertTrue(response['status'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
