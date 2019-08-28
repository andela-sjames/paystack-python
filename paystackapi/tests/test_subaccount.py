import httpretty

from paystackapi.tests.base_test_case import BaseTestCase
from paystackapi.subaccount import SubAccount


class TestSubAccount(BaseTestCase):

    @httpretty.activate
    def test_subaccount_create(self):
        pass
