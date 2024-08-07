## Subscription

##### `Subscription.create(customer, plan, authorization, start_date)` - Create a subscription.

```python
from paystackapi.subscription import Subscription
response = Subscription.create(customer='CUS_xnxdt6s1zg1f4nx',
                               plan='Pln_2yudUnIds2p',
                               authorization='34',
                               start_date=None)
```

*Arguments*
- `customer`: Customer's email address or customer code.
- `plan`: Plan code.
- `authorization`: customers authorization code.
- `start_date`:  the date for the first debit. (ISO 8601 format)

*Returns*

JSON data from paystack API.

##### `Subscription.fetch(subscription_id)` - Fetch a subscription.

```python
from paystackapi.subscription import Subscription
response = Subscription.fetch(subscription_id=4033)
```

*Arguments*
- `subscription_id`: subscription ID.

*Returns*

JSON data from paystack API.


##### `Subscription.list()` - List subscriptions.

```python
from paystackapi.subscription import Subscription
response = Subscription.list()
```

*Optional Arguments*

- `perPage`: Number of results per page.
- `page`: Pagination page number. 
- `customer`: Customer ID
- `plan`: Plan ID

*Returns*

JSON data from paystack API.

##### `Subscription.disable(code="SUB_vsyqdmlzble3uii",token="d7gofp6yppn3qz7")` - Disable a subscription.

```python
from paystackapi.subscription import Subscription
response = Subscription.disable(code="SUB_vsyqdmlzble3uii",
                                token="d7gofp6yppn3qz7")
```

*Arguments*

*Arguments*
- `code`: Subscription code.
- `token`: Email token.


*Returns*

JSON data from paystack API.

##### `Subscription.enable(code="SUB_vsyqdmlzble3uii",token="d7gofp6yppn3qz7")` - Enable a subscription.

```python
from paystackapi.subscription import Subscription
response = Subscription.enable(code="SUB_vsyqdmlzble3uii",
                                token="d7gofp6yppn3qz7")
```

*Arguments*
- `code`: Subscription code.
- `token`: Email token.


*Returns*

JSON data from paystack API.
