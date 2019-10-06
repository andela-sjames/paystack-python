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

##### `Customer.list()` - List paystack customers

```python
from paystackapi.customer import Customer
response = Customer.list()
```

*Arguments*

No argument required.

*Returns*

JSON data from paystack API.

##### `Customer.update(customer_id, first_name=None, last_name=None, email=None, phone=None)` - Update paystack customer data by id.

```python
from paystackapi.customer import Customer
response = Customer.update(customer_id=24, first_name=None,
                           last_name=None, email=None,
                           phone=None)
```

*Arguments*
- `customer_id`: paystack customer id.
- `first_name`: customer's first name(optional).
- `last_name`: customer's last name(optional).
- `email`: customer's email address(optional).
- `phone`: customer's phone number(optional).

*Returns*

JSON data from paystack API.
