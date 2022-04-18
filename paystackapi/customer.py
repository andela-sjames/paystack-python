"""Script used to define the paystack Customer class."""

from paystackapi.base import PayStackBase


class Customer(PayStackBase):
    """docstring for Customer."""

    @classmethod
    def create(cls, **kwargs):
        """
        Function defined to create customer.

        Args:
            first_name: customer's first name.
            last_name: customer's last name.
            email: customer's email address.
            phone:customer's phone number.

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('customer', data=kwargs,)

    @classmethod
    def get(cls, customer_id):
        """
        Static method defined to get customers by id.

        Args:
            customer_id: paystack customer id.
        Returns:
            Json data from paystack API.
        """
        return cls().requests.get(f"customer/{customer_id}")

    @classmethod
    def list(cls, **kwargs):
        """
        Static method defined to list paystack customers.

        Args:
            perPage: Specify how many records you want to retrieve per page.
                If not specify we use a default value of 50. (Integer)

            page: Specify exactly what page you want to retrieve.
                defaults to 1 if not present(Integer)

            from: A timestamp from which to start listing customers 
                e.g. 2016-09-24T00:00:05.000Z, 2016-09-21 (datetime)

            to:   A timestamp at which to stop listing customers 
                e.g. 2016-09-24T00:00:05.000Z, 2016-09-21 (datetime)

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get('customer', qs=kwargs,)

    @classmethod
    def update(cls, customer_id, **kwargs):
        """
        Static method defined to update paystack customer data by id.

        Args:
            customer_id: paystack customer id.
            first_name: customer's first name(optional).
            last_name: customer's last name(optional).
            email: customer's email address(optional).
            phone:customer's phone number(optional).

        Returns:
            Json data from paystack API.
        """
        return cls().requests.put(f"customer/{customer_id}", data=kwargs,)
