## Verification

##### `Verification.verify_bvn(bvn)` - verify a customer's BVN

```python
from paystackapi.verification import Verification
response = Verification.verify_bvn(account_number='1234567890')
```

*Arguments*

- `bvn`: customer's bvn number

*Returns*

JSON data from paystack API.


##### `Verification.verify_bvn_match(bvn)` - verify BVN match with account number, first name and last name

```python
from paystackapi.verification import Verification
response = Verification.verify_bvn_match(bvn='1234567890',account_number='34334343',bank_code='34343' )
```

*Arguments*

- `bvn`:             customer's bvn number
- `account_number`:  customer's account number
- `bank_code`:       customer's bank code
- `first_name`:      customer's first name (Optional)
- `last_name`:       customer's last name (Optional)
- `middle_name`:     customer's middle name (Optional)

*Returns*

JSON data from paystack API.


##### `Verification.verify_account(account_number)` - verify a customer's BVN

```python
from paystackapi.verification import Verification
response = Verification.verify_account(account_number='1234567890')
```

*Arguments*

- `account_number`: customer's account number

*Returns*

JSON data from paystack API.


##### `Verification.verify_card_bin(card_bin)` - verify a customer's card bin

```python
from paystackapi.verification import Verification
response = Verification.verify_card_bin(card_bin='001')
```

*Arguments*

- `card_bin`: customer's card bin

*Returns*

JSON data from paystack API.


##### `Verification.verify_phone(verification_type, phone, callback_url)` - verify a customer's phone number

```python
from paystackapi.verification import Verification
response = Verification.verify_phone(
    verification_type='truecaller',
    phone='090123456890,
    callback_url='https://google.com'
)
```

*Arguments*

- `verification_type`:  phone number verification type
- `phone`:              phone number to be verified
- `callback_url`:       callback url to send verification details to

*Returns*

JSON data from paystack API.