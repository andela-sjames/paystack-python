## Transaction Split

#### `TransactionSplit.create(**kwargs)` - Create a Transaction split

_Usage_

```python
from paystackapi.transaction_split import TransactionSplit
response = TransactionSplit.create(
            name="Test Biz 123",
            type="percentage",
            currency="xxxxxxxxx",
            subaccounts="[{'subaccount': 'ACCT_4hl4xenwpjy5wb', 'share':40 },...]",
            bearer_type="account"
        )
```

_Arguments_

- `name`: Name of the transaction split
- `type`: The type of transaction split you want to create (percentage or flat)
- `currency`: One of NGN, GHS, ZAR, or USD
- `subaccounts`: A list of object containing subaccount code and number of shares
- `bearer_type`: One of subaccount, account, all-proportional, or all.
- `bearer_subaccount`: Subaccount code
- `**kwargs`

_Returns_

JSON data from Paystack API.

#### `TransactionSplit.list(perPage, page)` - List or search for the transaction splits available on your integration.

_Usage_

```python
from paystackapi.transaction_split import TransactionSplit
response = TransactionSplit.list(perPage=3, page=1)
```

_Arguments_

- `perPage`: Records you want to retrieve per page (Integer)
- `page`: Which page you want to retrieve (Integer)
- `**kwargs`

_Returns_

JSON data from Paystack API.

#### `TransactionSplit.fetch(split_id)` - Get details of a split in your integration.

_Usage_

```python
from paystackapi.transaction_split import TransactionSplit
response = TransactionSplit.fetch(split_id=14551)
```

_Arguments_

- `split_id`: Split ID

_Returns_

JSON data from Paystack API.

#### `TransactionSplit.update(split_id, **kwargs)` - Update transaction split details in your integration

_Usage_

```python
from paystackapi.transaction_split import TransactionSplit
response = TransactionSplit.update(
            split_id=45411,
            **kwargs
        )
```

_Arguments_

- `split_id`: Slit ID
- `name`: Name of the transaction split
- `active`: True or False
- `subaccounts`: A list of object containing subaccount code and number of shares
- `bearer_type`: Any of subaccount | account | all-proportional | all
- `bearer_subaccount`: Subaccount code
- `**kwargs`

_Returns_

JSON data from Paystack API.

#### `TransactionSplit.remove_split_subaccount(split_id, **kwargs)` - Remove a subaccount from a transaction split.

_Usage_

```python
from paystackapi.transaction_split import TransactionSplit
response = TransactionSplit.remove_split_subaccount(
            split_id=45411,
            **kwargs
        )
```

_Arguments_

- `split_id`: Split ID
- `subaccount`: This is the subaccount code
- `**kwargs`

_Returns_

JSON data from Paystack API.

#### `TransactionSplit.add_or_update_split_subaccount(split_id, **kwargs)` - Add a subaccount to a transaction split or update the share of an existing subaccount in a transaction split.

_Usage_

```python
from paystackapi.transaction_split import TransactionSplit
response = TransactionSplit.add_or_update_split_subaccount(
            split_id=45411,
            **kwargs
        )
```

_Arguments_

- `split_id`: Split ID
- `subaccount`: This is the sub account code
- `share`: This is the transaction share for the subaccount
- `**kwargs`

_Returns_

JSON data from Paystack API.
