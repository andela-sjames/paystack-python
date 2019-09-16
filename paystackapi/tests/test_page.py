import httpretty

from paystackapi.tests.base_test_case import BaseTestCase
from paystackapi.page import Page


class TestPage(BaseTestCase):

    @httpretty.activate
    def test_page_create(self):
        """Method defined to test page creation."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/page"),
            content_type='text/json',
            body='{"status": true, "message": "Page created"}',
            status=201,
        )

        response = Page.create(
            name="New test product One"
        )
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_page_list(self):
        """Method defined to test page list method."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/page"),
            content_type='text/json',
            body='{"status": true, "message": "Pages retrieved"}',
            status=201,
        )

        response = Page.list(perPage=3, page=1)
        self.assertEqual(response['status'], True)
    
    @httpretty.activate
    def test_page_fetch(self):
        """Method defined to test page fetch method."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/page/5nApBwZkvY"),
            content_type='text/json',
            body='{"status": true, "message": "Page retrieved"}',
            status=201,
        )

        response = Page.fetch(id_or_slug="5nApBwZkvY")
        self.assertEqual(response['status'], True)

    @httpretty.activate
    def test_page_update(self):
        """Method defined to test page update method."""
        httpretty.register_uri(
            httpretty.PUT,
            self.endpoint_url("/page/5nApBwZkvY"),
            content_type='text/json',
            body='{"status": true, "message": "page updated"}',
            status=201,
        )

        response = Page.update(id_or_slug="5nApBwZkvY", name="new page name")
        self.assertEqual(response['status'], True)

    @httpretty.activate
    def test_is_slug_available(self):
        """Method defined to test_is_slug_available method."""
        httpretty.register_uri(
            httpretty.PUT,
            self.endpoint_url("/page/check_slug_availability/5nApBwZkvY"),
            content_type='text/json',
            body='{"status": true, "message": "Slug is available"}',
            status=201,
        )

        response = Page.is_slug_available(slug="5nApBwZkvY")
        self.assertEqual(response['status'], True)

    @httpretty.activate
    def test_add_products(self):
        """Method defined to test add_products method."""
        httpretty.register_uri(
            httpretty.PUT,
            self.endpoint_url("/page/23/product"),
            content_type='text/json',
            body='{"status": true, "message": "Products added to page"}',
            status=201,
        )

        response = Page.add_products(payment_page_id=23, product=[[473, 292]])
        self.assertEqual(response['status'], True)
