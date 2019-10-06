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
