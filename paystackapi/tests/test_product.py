import httpretty

from paystackapi.tests.base_test_case import BaseTestCase
from paystackapi.product import Product


class TestProduct(BaseTestCase):

    @httpretty.activate
    def test_product_create(self):
        """Method defined to test product creation."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/product"),
            content_type='text/json',
            body='{"status": true,  "message": "Product successfully created"}',
            status=201,
        )

        response = Product.create(
            name="Product pypaystack test", description="my test description",
            price=500000, currency="NGN"
        )
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_product_list(self):
        """Function defined to test Product list method."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/product"),
            content_type='text/json',
            body='{"status": true, "message": "Products retrieved", "data":[{}], "meta":{}}',
            status=201,
        )

        response = Product.list()
        self.assertEqual(response['status'], True)

    @httpretty.activate
    def test_product_fetch(self):
        """Function defined to test Product fetch method."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/product/5499"),
            content_type='text/json',
            body='{"status": true, "message": "Products retrieved", "data":[{}]}',
            status=201,
        )

        response = Product.fetch(5499)
        self.assertEqual(response['status'], True)

    @httpretty.activate
    def test_product_update(self):
        """Function defined to test Product update method."""
        httpretty.register_uri(
            httpretty.PUT,
            self.endpoint_url("/product/5499"),
            content_type='text/json',
            body='{"status": true, "message": "Products retrieved", "data":[{}]}',
            status=201,
        )

        response = Product.update(product_id=5499, name="Product pypaystack test",
            description="my test description", price=500000000,
            currency="USD"
        )
        self.assertEqual(response['status'], True)