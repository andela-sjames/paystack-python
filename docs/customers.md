## Customers

##### `Customer.create(first_name, last_name, email, phone)` - Create customer

```python
from paystackapi.customer import Customer
response = Customer.create(first_name='first_name',
                           last_name='last_name',
                           email='email', phone='phone')
```

*Arguments*

- `first_name`: customer's first name.
- `last_name`: customer's last name.
- `email`: customer's email address.
- `phone`: customer's phone number.

*Returns*

JSON data from paystack API.

##### `Customer.get(customer_id)` - Get customers by id

```python
from paystackapi.customer import Customer
response = Customer.get(customer_id=24)
```

*Arguments*

- `id`: paystack customer id

*Returns*

JSON data from paystack API.

##### `Customer.list(perPage=50, page=6)` - List Paystack customers

```python
from paystackapi.customer import Customer
response = Customer.list(perPage=50, page=6)
```

*Arguments*

- `perPage`: Specify how many records you want to retrieve per page.
            If not specified we use a default value of 50. (Integer)

- `page`: Specify exactly what page you want to retrieve.
          defaults to 1 if not present(Integer)

- `from`: A timestamp from which to start listing customers.
          e.g. 2016-09-24T00:00:05.000Z, 2016-09-21 (datetime)

- `to`:   A timestamp at which to stop listing customers.
        e.g. 2016-09-24T00:00:05.000Z, 2016-09-21 (datetime)

*Returns*

JSON data from paystack API.

##### `Customer.update(customer_id, first_name=None, last_name=None, email=None, phone=None)` - Update paystack customer data by ID.

```python
from paystackapi.customer import Customer
response = Customer.update(customer_id=24, first_name=None,
                           last_name=None, email=None,
                           phone=None)
```

*Arguments*
- `customer_id`: paystack customer ID.
- `first_name`: customer's first name(optional).
- `last_name`: customer's last name(optional).
- `email`: customer's email address(optional).
- `phone`: customer's phone number(optional).

*Returns*

JSON data from the Paystack API.
