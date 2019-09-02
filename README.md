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

## Transactions

##### `Transaction.initialize(reference, amount, email, plan)` - Initialize transaction.

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
- `plan`: Specified plan (optional)

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
- `authorization_code`: Authorization code for the transaction
- `email`: Email Address of the user with the authorization code
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
response = Transaction.list()
```

*Arguments*

No argument required.

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

##### `Transaction.verify(reference)` - Verify transactions.

```python
from paystackapi.transaction import Transaction
response = Transaction.verify(reference='reference')
```

*Arguments*

- `reference`: a unique value needed for transaction.

*Returns*

JSON data from paystack API.


## Plans

##### `Plan.create(name, description, amount, interval, send_invoices, send_sms, hosted_page, hosted_page_url, hosted_page_summary, currency)` - Create a plan

```python
from paystackapi.plan import Plan
response = Plan.create(name='value', description='value',
                       amount=amount, interval='value',
                       send_invoices='value',
                       send_sms='value',
                       hosted_page='value',
                       hosted_page_url='value',
                       hosted_page_summary='value',
                       currency='value')
```

*Arguments*

- `name`: plan's name.
- `description`: description of the plan.
- `amount`: amount for the plan in kobo
- `interval`: plan's interval(daily...etc)
- `send_invoices`: boolean
- `send_sms`: (optional)
- `hosted_page`: (optional)
- `hosted_page_url`: url of hosted page (optional)
- `hosted_page_summary`: summary of the hosted page
- `currency`: plans currency (NGN)

*Returns*

JSON data from paystack API.

##### `Plan.get(plan_id)` - Get a single plan.

```python
from paystackapi.plan import Plan
response = Plan.get(plan_id=25)
```

*Arguments*

- `id`: paystack plan id.

*Returns*

JSON data from paystack API.

##### `Plan.list()` - List paystack plan

```python
from paystackapi.plan import Plan
response = Plan.list()
```

*Arguments*

No argument required.

*Returns*

JSON data from paystack API.

##### `Plan.update(plan_id=88, name=None, description=None, amount=None, interval=None, send_invoices=None, send_sms=None, hosted_page=None, hosted_page_url=None, hosted_page_summary=None, currency=None)` - Update paystack plan

```python
from paystackapi.plan import Plan
response = Plan.update(plan_id=23, name=None, description=None,
                       amount=None, interval=None,
                       send_invoices=None, send_sms=None,
                       hosted_page=None, hosted_page_url=None,
                       hosted_page_summary=None, currency=None)
```

*Arguments*

- `plan_id`: plan identity number.
- `name`: name of plan
- `description`: plan description(optional)
- `amount`: plan amount in Kobo
- `interval`: plan interval9(monthly, yearly, quarterly...etc)
- `send_invoice`: (optional)
- `send_sms`: (optional)
- `hosted_page`: (optional)
- `hosted_page_url`: (optional)
- `hosted_page_summary`: (optional)
- `currency`: Naira in kobo(NGN)

*Returns*

JSON data from paystack API.


## Customers

##### `Customer.create(first_name, last_name, email, phone)` - Create customer

```python
from paystackapi.customer import Customer
response = Customer.create(first_name='first_name',
                           last_name='last_name',
                           email='email', phone='phone')
```

*Arguments*

- `first_name`: customer's first name.
- `last_name`: customer's last name.
- `email`: customer's email address.
- `phone`: customer's phone number.

*Returns*

JSON data from paystack API.

##### `Customer.get(customer_id)` - Get customers by id

```python
from paystackapi.customer import Customer
response = Customer.get(customer_id=24)
```

*Arguments*

- `id`: paystack customer id

*Returns*

JSON data from paystack API.

##### `Customer.list()` - List paystack customers

```python
from paystackapi.customer import Customer
response = Customer.list()
```

*Arguments*

No argument required.

*Returns*

JSON data from paystack API.

##### `Customer.update(customer_id, first_name=None, last_name=None, email=None, phone=None)` - Update paystack customer data by id.

```python
from paystackapi.customer import Customer
response = Customer.update(customer_id=24, first_name=None,
                           last_name=None, email=None,
                           phone=None)
```

*Arguments*
- `customer_id`: paystack customer id.
- `first_name`: customer's first name(optional).
- `last_name`: customer's last name(optional).
- `email`: customer's email address(optional).
- `phone`: customer's phone number(optional).

*Returns*

JSON data from paystack API.

## Subscription

##### `Subscription.create(customer, plan, authorization, start_date)` - Create subscription.

```python
from paystackapi.subscription import Subscription
response = Subscription.create(customer='CUS_xnxdt6s1zg1f4nx',
                               plan='Pln_2yudUnIds2p',
                               authorization='34',
                               start_date=None)
```

*Arguments*
- `customer`: Customer's email address or customer code.
- `plan`: Plan code.
- `authorization`: customers authorization code.
- `start_date`:  the date for the first debit. (ISO 8601 format)

*Returns*

JSON data from paystack API.

##### `Subscription.fetch(subscription_id)` - Fetch subscription.

```python
from paystackapi.subscription import Subscription
response = Subscription.fetch(subscription_id=4033)
```

*Arguments*
- `subscription_id`: subscription id.

*Returns*

JSON data from paystack API.


##### `Subscription.list()` - List subscriptions.

```python
from paystackapi.subscription import Subscription
response = Subscription.list()
```

*Arguments*

No argument required.

*Returns*

JSON data from paystack API.

##### `Subscription.disable(code="SUB_vsyqdmlzble3uii",token="d7gofp6yppn3qz7")` - Disable subscriptions.

```python
from paystackapi.subscription import Subscription
response = Subscription.disable(code="SUB_vsyqdmlzble3uii",
                                token="d7gofp6yppn3qz7")
```

*Arguments*

*Arguments*
- `code`: Subscription code.
- `token`: Email token.


*Returns*

JSON data from paystack API.

##### `Subscription.enable(code="SUB_vsyqdmlzble3uii",token="d7gofp6yppn3qz7")` - Enable subscriptions.

```python
from paystackapi.subscription import Subscription
response = Subscription.enable(code="SUB_vsyqdmlzble3uii",
                                token="d7gofp6yppn3qz7")
```

*Arguments*
- `code`: Subscription code.
- `token`: Email token.


*Returns*

JSON data from paystack API.

## Verification

##### `Verification.verify_bvn(bvn)` - verify a customer's BVN

```python
from paystackapi.verification import Verification
response = Verification.verify_bvn(bvn='1234567890')
```

*Arguments*

- `bvn`: customer's bvn number

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

Refunds
-------
#### `Refund.create(**kwargs)` - This creates a refund which is then processed by the Paystack team

```python
from paystackapi.refund import Refund
response = Refund.create(**kwargs)

```
*Arguments*
- `transaction`: Transaction reference or id
- `amount`: How much in kobo to be refunded to the customer - Optional
- `currency`: Three-letter ISO currency - Optional
- `customer_note`: Customer reason - Optional
- `merchant_note`: Merchant reason - Optional

*Returns*

JSON data from paystack API.


#### `Refund.list(**kwargs)` - Get a list of refunds

```python
from paystackapi.refund import Refund
response = Refund.list(**kwargs)

```
*Arguments*
- `reference`: Identifier for transaction to be refunded - Optional
- `currency`: Three-letter ISO currency - Optional

*Returns*

JSON data from paystack API.

#### `Refund.fetch(refund_id)` - Get a refund by its id

```python
from paystackapi.refund import Refund
response = Refund.fetch(refund_id=1234)

```
*Arguments*
- `refund_id`: Refund ID

*Returns*

JSON data from paystack API.


Product
-------
#### `Product.create(**kwargs)` - Create a Product

*Usage*

```python
from paystackapi.product import Product
response = Product.create(name="Product pypaystack test",
						  description="my test description",
                          price=500000, currency="NGN", **kwargs)
```

*Arguments*

- `name`: Name of the product
- `description`: Description of product
- `price`: Price of the product, in kobo(Integer)
- `currency`: Currency in which amount should be charged
- **kwargs

*Returns*

JSON data from Paystack API.


#### `Product.list()` - list created Products

*Usage*

```python
from paystackapi.product import Product
response = Product.list()
```

*Arguments*

No argument required.

*Returns*

JSON data from Paystack API.


#### `Product.fetch(product_id)` - fetch created Products by id

*Usage*

```python
from paystackapi.product import Product
response = Product.fetch(product_id=5499)
```

*Arguments*

- `product_id`: Product id(integer).

*Returns*

JSON data from Paystack API.


#### `Product.update(product_id, **kwargs)` - update a created Product by id

*Usage*

```python
from paystackapi.product import Product
response = Product.update(product_id=5499, **kwargs)
```

*Arguments*

- `product_id`: Paystack product id.
- `name`: Name of the product
- `description`: Description of product
- `price`: Price of the product, in kobo(Integer)
- `currency`: Currency in which amount should be charged
- `**kwargs`

*Returns*

JSON data from Paystack API.


SubAccount
-------
#### `SubAccount.create(**kwargs)` - Create a SubAccount

*Usage*

```python
from paystackapi.subaccount import SubAccount
response = SubAccount.create(
            business_name="Test Biz 123",
            settlement_bank="Access Bank",
            account_number="xxxxxxxxx",
            percentage_charge="6.9"
        )
```

*Arguments*

- `business_name`: Name of business for subaccount
- `settlement_bank`: Name of Bank (accepted banks)
- `account_number`: NUBAN Bank Account number
- `percentage_charge`: Default percentage charged on subaccount?
- `**kwargs`

*Returns*

JSON data from Paystack API.

#### `SubAccount.list(perPage, page)` - List a SubAccount

*Usage*

```python
from paystackapi.subaccount import SubAccount
response = SubAccount.list(perPage=3, page=1)
```

*Arguments*

- `perPage`: Records you want to retrieve per page (Integer)
- `page`: What page you want to retrieve (Integer)
- `**kwargs`

*Returns*

JSON data from Paystack API.


#### `SubAccount.fetch(id_or_slug)` - Fetch a SubAccount

*Usage*

```python
from paystackapi.subaccount import SubAccount
response = SubAccount.fetch(id_or_slug="some_slug_like_subaccount_code_or_id)
```

*Arguments*

- `id_or_slug`: ID or Subaccount_Code

*Returns*

JSON data from Paystack API.


#### `SubAccount.update(id_or_slug, **kwargs)` - Update a SubAccount

*Usage*

```python
from paystackapi.subaccount import SubAccount
response = SubAccount.update(
            id_or_slug="some_slug_like_subaccount_code_or_id),
            **kwargs
        )
```

*Arguments*

- `id_or_slug`: ID or Subaccount_Code
- `business_name`: Name of business for subaccount
- `settlement_bank`: Name of Bank (accepted banks)
- `account_number`: NUBAN Bank Account number
- `percentage_charge`: Default percentage charged on subaccount?
- `**kwargs`

*Returns*

JSON data from Paystack API.

Payment Page
-------
#### `Page.create(name, **kwargs)` - Create a Page

*Usage*

```python
from paystackapi.page import Page
response = Page.create(
            name="New test product One"
        )
```

*Arguments*
- `name`: name of page
- `**kwargs`

*Returns*

JSON data from Paystack API.

#### `Page.list(perPage, page)` - List a Page

*Usage*

```python
from paystackapi.page import Page
response = Page.list(perPage=3, page=1)
```

*Arguments*
- `perPage`: records you want to retrieve per page (Integer)
- `page`: what page you want to retrieve (Integer)

*Returns*

JSON data from Paystack API.

#### `Page.fetch(id_or_slug)` - Fetch a Page

*Usage*

```python
from paystackapi.page import Page
response = Page.fetch(id_or_slug="5nApBwZkvY")
```

*Arguments*
- `id_or_slug`: id or slug

*Returns*

JSON data from Paystack API.

#### `Page.update(id_or_slug)` - Update a Page by id_or_slug

*Usage*

```python
from paystackapi.page import Page
response = Page.update(id_or_slug="5nApBwZkvY", **kwargs)
```

*Arguments*
- `id_or_slug`: id or slug
- `**kwargs`

*Returns*

JSON data from Paystack API.

#### `Page.is_slug_available(id_or_slug)` - Check Slug Availability

*Usage*

```python
from paystackapi.page import Page
response = Page.is_slug_available(slug="new_or_existing_slug")
```

*Arguments*
- `slug`: URL slug to be confirmed

*Returns*

JSON data from Paystack API.

#### `Page.add_products(id_or_slug)` - Add products to payment page

*Usage*

```python
from paystackapi.page import Page
response = Page.add_products(
				payment_page_id="new_or_existing_slug"
            	product=[123, 456, 457]
            )
```

*Arguments*

- `payment_page_id`: Id of the payment page (Integer)
- `product`: Ids of all the products i.e. [473, 292]

*Returns*

JSON data from Paystack API.

Settlements
-------
#### `Settlement.fetch(**kwargs)` - Fetch a Settlement

*Usage*

```python
from paystackapi.settlement import Settlement
response = Settlement.fetch(
            from="2016-09-12T00:00:00.000Z",
            to="2016-09-12T00:00:00.000Z",
            subaccount="subaccount"
        )
```

*Arguments*

- `start_date`: Lower bound of date range. Leave undefined to export settlement from day one.
- `end_date`: Upper bound of date range.Leave undefined to export settlements till date.
- `subaccount`: code to export only settlements for that subaccount. Set to none to export only transactions for the account.

*Returns*

JSON data from Paystack API.


Control Panel
-------------
#### `ControlPanel.fetch_payment_session_timeout()` - Fetch payment session timeout

*Usage*

```python
from paystackapi.cpanel import ControlPanel
response = ControlPanel.fetch_payment_session_timeout()
```

*Arguments*

No argument required.

*Returns*

JSON data from Paystack API.


#### `ControlPanel.update_payment_session_timeout(timeout)` - Update payment session timeout

*Usage*

```python
from paystackapi.cpanel import ControlPanel
response = ControlPanel.update_payment_session_timeout(timeout=30)
```

*Arguments*

- `timeout`: Time before stopping session (in seconds). Set to 0 to cancel session timeouts

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
