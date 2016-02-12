import unittest
import mock

from paystack.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        pass

    def test_create(self):
        with mock.patch('Customer.create') as mock_create:
            mock_create.return_value = {
                u'status': True, u'message': u'Customer created',
                u'data': {u'customer_code': u'CUS_jemg85nfijhrp1s',
                          u'first_name': u'samuel', u'last_name': u'james',
                          u'domain': u'test', u'integration': 100384,
                          u'phone': u'00000000000',
                          u'updatedAt': u'2016-02-12T12:25:19.960Z',
                          u'id': 4013, u'email': u'johndoe@andela.com',
                          u'createdAt': u'2016-02-12T12:25:19.960Z'}
            }

            response = Customer.create(
                'samuel', 'james', 'johndoe@andela.com', '00000000000')
            self.assertTrue(response.status)


    def test_get(self):
        pass

    def test_list(self):
        pass

    def test_update(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=1)
