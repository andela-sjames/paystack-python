# paystack-python
[![Coverage Status](https://coveralls.io/repos/github/andela-sjames/paystack-python/badge.svg?branch=develop)](https://coveralls.io/github/andela-sjames/paystack-python?branch=master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/andela-sjames/paystack-python/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/andela-sjames/paystack-python/?branch=master)
[![Circle CI](https://img.shields.io/badge/license-MIT-blue.svg)](https://img.shields.io/badge/license-MIT-blue.svg) [![Build Status](https://travis-ci.org/andela-sjames/paystack-python.svg?branch=master)](https://travis-ci.org/andela-sjames/paystack-python)
[![PyPI version](https://badge.fury.io/py/paystackapi.svg)](https://badge.fury.io/py/paystackapi)

Python plugin for [Paystack](https://paystack.com/)
View on [pypi.python.org](https://pypi.python.org/pypi/paystackapi)

# Installation
```
pip install paystackapi
```
# Instantiate Paystack

```python
from paystackapi.paystack import Paystack
paystack_secret_key = "5om3secretK3y"
paystack = Paystack(secret_key=paystack_secret_key)

# to use transaction class
paystack.transaction.list()

# to use customer class
paystack.customer.get(transaction_id)

# to use plan class
paystack.plan.get(plan_id)

# to use subscription class
paystack.subscription.list()
```

## DOC Reference: <https://developers.paystack.co/v2.0/reference>

##### Other methods can be found below...

# Static Use

To start using the Paystack Python API, you need to start by setting your secret key.

You can set your secret key in your environment by running:
```bash
export PAYSTACK_SECRET_KEY = 'your_secret_key'
```


> Don't forget to get your API key from [Paystack](https://paystack.com/) and assign to the variable `PAYSTACK_SECRET_KEY`


Charge
--------------------
#### `Charge.start_charge(**kwargs)` - Start a Chsrge

*Usage*

```python
from paystackapi.charge import Charge
response = Charge.start_charge(
            email="CUS_je02lbimlqixzax",
            amount=42000,
            metadata={
                "custom_fields": [
                    {
                        "value":"makurdi",
                        "display_name": "Donation for",
                        "variable_name": "donation_for"
                    },
                ],
            },
            bank={
                "code":"057",
                "account_number":"0000000000"
            },
            birthday="1995-12-23"
        )

```

*Arguments*

- `email`: Customer's email address
- `amount`: Amount in kobo
- `**kwargs`

*Returns*

JSON data from Paystack API.

#### `Charge.submit_pin(**kwargs)` - Submit PIN to continue a charge.

*Usage*

```python
from paystackapi.charge import Charge
response = Charge.submit_pin(
            pin="0987",
            reference="5bwib5v6anhe9xa",
        )
```

*Arguments*

- `pin`: PIN submitted by user
- `reference`: reference for transaction that requested pin

*Returns*

JSON data from Paystack API.


#### `Charge.submit_otp(**kwargs)` - Submit OTP to complete a charge.

*Usage*

```python
from paystackapi.charge import Charge
response = Charge.submit_otp(
            otp="0987",
            reference="5bwib5v6anhe9xa",
        )
```

*Arguments*

- `otp`: OTP submitted by user
- `reference`: reference for ongoing transaction

*Returns*

JSON data from Paystack API.


#### `Charge.submit_phone(**kwargs)` - Submit Phone when requested.

*Usage*

```python
from paystackapi.charge import Charge
response = Charge.submit_phone(
            phone="0XX4XX9X0XF",
            reference="5bwib5v6anhe9xa",
        )
```

*Arguments*

- `phone`: Phone submitted by user
- `reference` : reference for ongoing transaction
*Returns*

JSON data from Paystack API.

#### `Charge.submit_birthday(**kwargs)` - Submit Birthday when requested.

*Usage*

```python
from paystackapi.charge import Charge
response = Charge.submit_birthday(
            birthday="1975-12-23",
            reference="5bwib5v6anhe9xa",
        )
```

*Arguments*

- `birthday`: Birthday submitted by user
- `reference`: reference for ongoing transaction

*Returns*

JSON data from Paystack API.

#### `Charge.check_pending(reference)` - Check pending charge

*Usage*

```python
from paystackapi.charge import Charge
response = Charge.check_pending(
            reference="5bwib5v6anhe9xa",
        )
```

*Arguments*

- `reference`: The reference to check

*Returns*

JSON data from Paystack API.

TransferControl
--------------

#### `TransferControl.check_balance(**kwargs)` - Check Balance.

*Usage*

```python
from paystackapi.tcontrol import TransferControl
response = TransferControl.check_balance()

```

*Arguments*

No argument required.

*Returns*

JSON data from Paystack API.


#### `TransferControl.resend_otp(**kwargs)` - Resend OTP for Transfer.

*Usage*

```python
from paystackapi.tcontrol import TransferControl
response = TransferControl.resend_otp(
            transfer_code="TRF_vsyqdmlzble3uii",
            reason="Just do it."
        )
```

*Arguments*

- `transfer_code`: Transfer code
- `reason`: either resend_otp or transfer

*Returns*

JSON data from Paystack API.


#### `TransferControl.disable_otp_finalize(**kwargs)` - Finalize Disabling of OTP requirement for Transfers

*Usage*

```python
from paystackapi.tcontrol import TransferControl
response = TransferControl.disable_otp_finalize(
            otp="928783",
        )
```

*Arguments*

- `otp`: OTP sent to business phone to verify disabling OTP requirement

*Returns*

JSON data from Paystack API.


#### `TransferControl.disable_otp()` - Disable OTP requirement for Transfers

*Usage*

```python
from paystackapi.tcontrol import TransferControl
response = TransferControl.disable_otp()
```

*Arguments*

No arguments required

*Returns*

JSON data from Paystack API.

#### `TransferControl.enable_otp(**kwargs)` - Enable OTP requirement for Transfers

*Usage*

```python
from paystackapi.tcontrol import TransferControl
response = TransferControl.enable_otp()
```

*Arguments*

No arguments required

*Returns*

JSON data from Paystack API.


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


Miscellaneous
-------------

``Misc.list_banks()`` - List Banks

```python
   from paystackapi.misc import Misc
   response = Misc.list_banks()
```
*Returns*

JSON data from paystack API.
