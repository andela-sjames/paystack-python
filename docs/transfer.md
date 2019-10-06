Transfer
--------
#### `Transfer.initiate(**kwargs)` - Initiate a new Transfer.

*Usage*

```python
from paystackapi.transfer import Transfer
response = Transfer.initiate(
            source="balance",
            reason="Calm down",
            amount="3794800",
            recipient="RCP_gx2wn530m0i3w3m",
        )
```

*Arguments*

- `source`: Where should we transfer from? Only balance for now
- `amount`: Amount to transfer in kobo
- `currency`: Currency type to use
- `recipient`: Code for transfer recipient
- `**kwargs`

*Returns*

JSON data from Paystack API.

#### `Transfer.list(**kwargs)` - List a Transfer.

*Usage*

```python
from paystackapi.transfer import Transfer
response = Transfer.list(perPage=3,page=1)
```

*Arguments*

- `perPage`: records you want to retrieve per page (Integer)
- `page`: what page you want to retrieve (Integer)

*Returns*

JSON data from Paystack API.

#### `Transfer.fetch(id_or_code)` - Fetch a Transfer.

*Usage*

```python
from paystackapi.transfer import Transfer
response = Transfer.fetch(
            id_or_code="TRF_2x5j67tnnw1t98k",
        )
```

*Arguments*

- `id_or_code`: An ID or code for the transfer whose details you want to retrieve.

*Returns*

JSON data from Paystack API.

#### `Transfer.finalize(**kwargs)` - Finalize a Transfer.

*Usage*

```python
from paystackapi.transfer import Transfer
response = Transfer.finalize(
            transfer_code="TRF_2x5j67tnnw1t98k",
            otp="928783"
        )
```

*Arguments*

- `transfer_code`: Transfer code
- `otp`: OTP sent to business phone to verify transfer


*Returns*

JSON data from Paystack API.


#### `Transfer.initiate_bulk_transfer(**kwargs)` - Initiate a bulk Transfer.

*Usage*

```python
from paystackapi.transfer import Transfer
response = Transfer.initiate_bulk_transfer(
            currency="TRF_2x5j67tnnw1t98k",
            source="928783",
            transfers=[
                {
                    "amount": 50000,
                    "recipient": "RCP_db342dvqvz9qcrn"
                },
                {
                    "amount": 50000,
                    "recipient": "RCP_db342dvqvz9qcrn"
                }
            ]
        )
```

*Arguments*
```Text
currency: Currency type to use
source: Where should we transfer from? Only balance for now
transfers: Array of transfer objects [
    {
        amount: Amount to transfer in kobo
        recipient: Code for transfer recipient
    },
    {
        amount: Amount to transfer in kobo
        recipient: Code for transfer recipient
    }
]
```
*Returns*

JSON data from Paystack API.


#### `Transfer.verify(**kwargs)` - Finalize a Transfer.

*Usage*

```python
from paystackapi.transfer import Transfer
response = Transfer.verify(
            reference="ref_demo",
        )
```

*Arguments*
- `reference`: Transfer reference


*Returns*

JSON data from Paystack API.
