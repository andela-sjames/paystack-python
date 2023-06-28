Transfer Recipient
---------------------
#### `TransferRecipient.create(**kwargs)` - Create a new Transfer Recipient.

*Usage*

```python
from paystackapi.trecipient import TransferRecipient
response = TransferRecipient.create(
            type="nuban",
            name="Zombie",
            description="Zombier",
            account_number="01000000010",
            bank_code="044",
        )
```

*Arguments*

- `type`: Recipient Type (Only nuban at this time).
- `name`: A name for the recipient.
- `account_number`: Required if type is nuban.
- `bank_code`: Required if type is nuban. You can get the list of Bank Codes by calling the List Banks endpoint.
- `**kwargs`

*Returns*

JSON data from Paystack API.


#### `TransferRecipient.list(**kwargs)` - list Transfer Recipient.

*Usage*

```python
from paystackapi.trecipient import TransferRecipient
response = TransferRecipient.list(perPage=3, page=1)
```

*Arguments*

- `perPage`: records you want to retrieve per page (Integer).
- `page`: which page you want to retrieve (Integer).


*Returns*

JSON data from Paystack API.
