## Transactions
`https://paystack.com/docs/api/transaction/`


##### `Transaction.initialize(reference, amount, email, plan)` - Initialize a transaction.

*Usage*

```python
from paystackapi.transaction import Transaction
response = Transaction.initialize(reference='reference',
                                  amount='amount', email='email')
```

*Arguments*

- `reference`: Unique transaction reference
- `amount`: Amount
- `email`: Email address
- `plan`: A apecified plan (optional)

*Returns*

JSON data from Paystack API.

##### `Transaction.charge(reference, authorization_code, email, amount)` - Charge authorization.

```python
from paystackapi.transaction import Transaction
response = Transaction.charge(reference='reference',
                              authorization_code='authorization_code',
                              email='email',
                              amount='amount')
```

*Arguments*

- `reference`: Unique transaction reference
- `authorization_code`: The authorization code for the transaction
- `email`: The email Address of the user with the authorization code
- `amount`: Amount in kobo

*Returns*

JSON data from Paystack API.

##### `Transaction.charge_token(reference, token, email, amount)` - Charge Token.

```python
from paystackapi.transaction import Transaction
response = Transaction.charge_token(reference='reference',
                                    token='token', email='email',
                                    amount='amount')
```

*Arguments*

- reference: unique transaction reference
- token: paystack token
- email: Email Address
- amount: Amount in Kobo

*Returns*

JSON data from Paystack API.

##### `Transaction.get(transaction_id)` - Get a single transaction.

```python
from paystackapi.transaction import Transaction
response = Transaction.get(transaction_id=23)
```

*Arguments*

- `id`: Transaction id(integer).

*Returns*

JSON data from paystack API.

##### `Transaction.list()` - List transactions.

```python
from paystackapi.transaction import Transaction
response = Transaction.list(perPage=3,page=1)
```

*Arguments* 

- `customer`: Specify an ID for the customer whose transactions you want to retrieve (optional)
- `status`: Filter transactions by status ('failed', 'success', 'abandoned') (optional)
- ...

*Returns*

JSON data from paystack API.

##### `Transaction.totals()` - Get totals.

```python
from paystackapi.transaction import Transaction
response = Transaction.totals()
```
*Arguments*

No argument required.

*Returns*

JSON data from paystack API.

##### `Transaction.verify(reference)` - Verify a transaction.

```python
from paystackapi.transaction import Transaction
response = Transaction.verify(reference='reference')
```

*Arguments*

- `reference`: a unique value needed for transaction.

*Returns*

JSON data from paystack API.
