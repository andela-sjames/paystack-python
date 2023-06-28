Refunds
-------
#### `Refund.create(**kwargs)` - Create a refund, which is then processed by the Paystack team.

```python
from paystackapi.refund import Refund
response = Refund.create(**kwargs)

```
*Arguments*
- `transaction`: Transaction reference or id
- `amount`: Amount in kobo to be refunded to the customer (optional).
- `currency`: Three-letter ISO currency (Optional)
- `customer_note`: Customer reason 
(Optional)
- `merchant_note`: Merchant reason (Optional)

*Returns*

JSON data from paystack API.


#### `Refund.list(**kwargs)` - Get a list of refunds.

```python
from paystackapi.refund import Refund
response = Refund.list(**kwargs)

```
*Arguments*
- `reference`: Identifier for transaction to be refunded (Optional)
- `currency`: Three-letter ISO currency - (Optional)

*Returns*

JSON data from paystack API.

#### `Refund.fetch(refund_id)` - Get a refund by its ID

```python
from paystackapi.refund import Refund
response = Refund.fetch(refund_id=1234)

```
*Arguments*
- `refund_id`: Refund ID

*Returns*

JSON data from paystack API.
