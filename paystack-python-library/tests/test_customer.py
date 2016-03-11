"""Script defined to test the Customer class."""


import unittest
import mock

from paystack.customer import Customer


class TestCustomer(unittest.TestCase):
    """Class to test customer actions."""

    def test_create(self):
        """Method defined to test customer creation."""
        with mock.patch('paystack.customer.Customer.create') as mock_create:
            mock_create.return_value = {
                'status': True, 'message': 'Customer created',
                'data': {'customer_code': 'CUS_jemg85nfijhrp1s',
                         'first_name': 'samuel', 'last_name': 'james',
                         'domain': 'test', 'integration': 100384,
                         'phone': '00000000000',
                         'updatedAt': '2016-02-12T12:25:19.960Z',
                         'id': 4013, 'email': 'johndoe@andela.com',
                         'createdAt': '2016-02-12T12:25:19.960Z'}
            }

            response = Customer.create(
                'samuel', 'james', 'johndoe@andela.com', '00000000000')
            self.assertTrue(response['status'])

    def test_get(self):
        """Function defined to test Customer get method."""
        with mock.patch('paystack.customer.Customer.get') as mock_get:
            mock_get.return_value = {
                'status': True, 'message': 'Customer retrieved',
                'data': {'total_transactions': 0,
                         'customer_code': 'CUS_jemg85nfijhrp1s',
                         'first_name': 'samuel', 'last_name': 'james',
                         'authorizations': [], 'total_transaction_value': 0,
                         'subscriptions': [], 'transactions': [],
                         'domain': 'test', 'id': 4013,
                         'phone': '00000000000',
                         'updatedAt': '2016-02-12T12:25:19.000Z',
                         'integration': 100384, 'email': 'johndoe@andela.com',
                         'createdAt': '2016-02-12T12:25:19.000Z',
                         'metadata': None}
            }

            response = Customer.get(4013)
            self.assertEqual(response['status'], True)

    def test_list(self):
        """Function defined to test paystack customer list method."""
        with mock.patch('paystack.customer.Customer.list') as mock_list:
            mock_list.return_value = {
                'status': True, 'message': 'Customers retrieved',
                'meta': {'skipped': 0, 'total': 1, 'page': 1,
                         'perPage': 50, 'pageCount': 1},
                'data': [{'customer_code': 'CUS_jemg85nfijhrp1s',
                          'first_name': 'samuel', 'last_name': 'james',
                          'integration': 100384, 'id': 4013,
                          'phone': '08030495860', 'domain': 'test',
                          'updatedAt': '2016-02-12T12:25:19.000Z',
                          'email': 'johndoe@andela.com',
                          'createdAt': '2016-02-12T12:25:19.000Z',
                          'metadata': None}]
            }

            response = Customer.list()
            self.assertEqual(response['status'], True)

    def test_update(self):
        """Function defined to test paystack customer update."""
        with mock.patch('paystack.customer.Customer.update') as mock_update:
            mock_update.return_value = {
                'status': True, 'message': 'Customer updated',
                'data': {'customer_code': 'CUS_jemg85nfijhrp1s',
                         'first_name': 'andela', 'last_name': 'james',
                         'domain': 'test', 'id': 4013, 'phone': '08030495860',
                         'updatedAt': '2016-02-12T14:28:25.000Z',
                         'integration': 100384,
                         'email': 'samuel.james@andela.com',
                         'createdAt': '2016-02-12T12:25:19.000Z',
                         'metadata': None}
            }

            response = Customer.update(4013, 'andela')
            self.assertEqual(response['status'], True)

if __name__ == '__main__':
    unittest.main(verbosity=2)
