BulkCharge
--------------

#### `BulkCharge.initiate_bulk_charge(bulkcharge)` - Initiate Bulk Charge.

*Usage*

```python
from paystackapi.bulkcharge import BulkCharge
response = BulkCharge.initiate_bulk_charge(
            bulkcharge=[
                {"authorization": "AUTH_n95vpedf", "amount": 2500}, 
                {"authorization": "AUTH_ljdt4e4j", "amount": 1500}
            ]
        )
```

*Arguments*
- `authorization`: Authorization token
- `amount`: Amount in kobo

*Returns*

JSON data from Paystack API.


#### `BulkCharge.list(**kwargs)` - List Bulk Charge Batches created by the integration.

*Usage*

```python
from paystackapi.bulkcharge import BulkCharge
response = BulkCharge.list()
```

*Arguments*

- `perPage`: Number of transfer listed per page for pagination
- `page`: number of pages listed by pagination.

*Returns*

JSON data from Paystack API.


#### `BulkCharge.fetch_bulk_batch(id_or_code)` - This endpoint retrieves a specific batch code.

*Usage*

```python
from paystackapi.bulkcharge import BulkCharge
response = BulkCharge.fetch_bulk_batch(
            id_or_code="BCH_orj0ttn8vtp80hx"
        )
```

*Arguments*
- `id_or_code`: An ID or code for the transfer whose details you want to retrieve.

*Returns*

JSON data from Paystack API.

#### `BulkCharge.fetch_charges_batch(id_or_code, **kwargs)` - Fetch the charges associated with a specified batch code.

*Usage*

```python
from paystackapi.bulkcharge import BulkCharge
response = BulkCharge.fetch_charges_batch(
            id_or_code="BCH_orj0ttn8vtp80hx"
        )
```

*Arguments*

- `id_or_code`: An ID or code for the batch whose charges you want to retrieve.
- `status`: pending, success or failed
- `perPage`: Number of transfers listed per page for pagination
- `page`: number of pages listed by pagination.

*Returns*

JSON data from Paystack API.

#### `BulkCharge.pause_bulk_batch(batch_code)` - Pause the proccessing of an ongoing bulk charge batch.

*Usage*

```python
from paystackapi.bulkcharge import BulkCharge
response = BulkCharge.pause_bulk_batch(
            batch_code="BCH_orj0ttn8vtp80hx"
        )
```

*Arguments*
- `batch_code`: code of the batch to be paused


*Returns*

JSON data from Paystack API.


#### `BulkCharge.resume_bulk_charge(batch_code)` - Resume the proccessing of an already paused bulk charge batch.

*Usage*

```python
from paystackapi.bulkcharge import BulkCharge
response = BulkCharge.resume_bulk_charge(
            batch_code="BCH_orj0ttn8vtp80hx"
        )
```

*Arguments*
- `batch_code`: code of the batch to be resumed

*Returns*

JSON data from Paystack API.
