Charge
--------------------
#### `Charge.start_charge(**kwargs)` - Start a charge

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

#### `Charge.submit_pin(**kwargs)` - Submit PIN to continue the charge.

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


#### `Charge.submit_otp(**kwargs)` - Submit OTP to complete the charge.

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


#### `Charge.submit_phone(**kwargs)` - Submit phone when requested.

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

#### `Charge.submit_birthday(**kwargs)` - Submit birthday when requested.

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
