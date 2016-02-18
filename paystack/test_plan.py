"""Script defined to test the Plan class."""


import unittest
import mock

from paystack.plan import Plan


class TestPlan(unittest.TestCase):
    """Class to test Plans."""

    def test_create(self):
        """Method defined to test plan creation."""
        with mock.patch('paystack.plan.Plan.create') as mock_create:
            mock_create.return_value = {
                'status': True, 'message': 'Plan created',
                'data': {
                        'plan_code': 'PLN_xj5fn3oc8cxzyid',
                        'domain': 'test',
                        'hosted_page_url': 'url',
                        'name': 'John Doe',
                        'interval': 'daily',
                        'send_sms': False,
                        'integration': 100300,
                        'currency': 'NGN',
                        'amount': 50000,
                        'send_invoices': False,
                        'createdAt': '2016-02-18T09:49:04.077Z',
                        'updatedAt': '2016-02-18T09:49:04.077Z',
                        'hosted_page_summary': 'details of the hosted page',
                        'id': 78,
                        'hosted_page': False,
                        'description': 'Payment plan for awesome people contributions'
                          }
            }

            response = Plan.create(
                "John Doe", "Payment plan for awesome people contributions", 50000, "daily", True, True, 'url', 'url',
                'details of the hosted page', 'NGN'
            )
            self.assertTrue(response['status'])

    def test_get(self):
        """Function defined to test Plan get method."""
        with mock.patch('paystack.plan.Plan.get') as mock_get:
            mock_get.return_value = {
                'status': True, 'message': 'Plan retrieved',
                'data': {
                        'domain': 'test',
                        'hosted_page_url': 'url',
                        'description': 'Payment plan for awesome people contributions',
                        'subscriptions': [

                        ],
                        'amount': 50000,
                        'interval': 'daily',
                        'send_sms': False,
                        'integration': 100300,
                        'currency': 'NGN',
                        'plan_code': 'PLN_xj5fn3oc8cxzyid',
                        'send_invoices': False,
                        'createdAt': '2016-02-18T09:49:04.000Z',
                        'updatedAt': '2016-02-18T09:49:04.000Z',
                        'hosted_page_summary': 'details of the hosted page',
                        'id': 78,
                        'hosted_page': False,
                        'name': 'John Doe'
                      }
            }

            response = Plan.get(78)
            self.assertEqual(response['status'], True)

    def test_list(self):
        """Function defined to test paystack plan list method."""
        with mock.patch('paystack.plan.Plan.list') as mock_list:
            mock_list.return_value = {
                'status': True, 'message': 'Plan retrieved',
                'meta': {'skipped': 0, 'total': 1, 'page': 1,
                         'perPage': 50, 'pageCount': 1},
                'data': [
                        {
                          'domain': 'test',
                          'hosted_page_url': None,
                          'description': None,
                          'subscriptions': [

                          ],
                          'amount': 10000,
                          'interval': 'monthly',
                          'send_sms': True,
                          'integration': 100300,
                          'currency': 'NGN',
                          'plan_code': 'PLN_0khzgl3c34sghbz',
                          'send_invoices': True,
                          'createdAt': '2016-02-12T11:43:48.000Z',
                          'updatedAt': '2016-02-12T11:43:48.000Z',
                          'hosted_page_summary': None,
                          'id': 60,
                          'hosted_page': False,
                          'name': 'API demo'
                        }]
            }

            response = Plan.list()
            self.assertEqual(response['status'], True)

    def test_update(self):
        """Function defined to test paystack plan update."""
        with mock.patch('paystack.plan.Plan.update') as mock_update:
            mock_update.return_value = {
                'status': True, 'message': 'Plan updated',
                'data': {
                        'domain': 'test',
                        'hosted_page_url': 'url',
                        'name': 'John Doe',
                        'interval': 'monthly',
                        'send_sms': False,
                        'amount': 70000,
                        'integration': 100300,
                        'currency': 'NGN',
                        'plan_code': 'PLN_xj5fn3oc8cxzyid',
                        'send_invoices': False,
                        'createdAt': '2016-02-18T09:49:04.000Z',
                        'updatedAt': '2016-02-18T12:00:53.000Z',
                        'hosted_page_summary': 'details of the hosted page',
                        'id': 78,
                        'hosted_page': False,
                        'description': 'Payment plan for awesome people contributions'
                      }
            }

            response = Plan.update(78, interval="monthly", amount=70000)
            self.assertEqual(response['status'], True)

if __name__ == '__main__':
    unittest.main(verbosity=2)
