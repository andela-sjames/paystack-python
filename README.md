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


Invoices
--------

#### `Invoice.create(**kwargs)` - Create a new invoice.

*Usage*

```python
from paystackapi.invoice import Invoice
response = Invoice.create(
            customer="CUS_je02lbimlqixzax",
            amount=42000,
            due_date="2019-05-08T00:00:00.000Z"
        )
```

*Arguments*

- `customer`: customer id or code
- `amount`: payment request amount.(Integer) Only useful if line items and tax values are ignored. Endpoint will throw a friendly warning if neither is available.
- `due_date`: ISO 8601 representation of request due date.
- `**kwargs`

*Returns*

JSON data from Paystack API.


#### `Invoice.list(**kwargs)` - list created invoice(s).

*Usage*

```python
from paystackapi.invoice import Invoice
response = Invoice.list(
            customer="CUS_je02lbimlqixzax",
            status="pending",
            currency="NGN",
            paid="false",
            include_archive="true"
        )
```

*Arguments*
- `customer`: filter by customer ID
- `status`: filter by invoice status
- `currency`: filter by currency
- `paid`: filter by paid invoice
- `include_archive`: include_archive

*Returns*

JSON data from Paystack API.

#### `Invoice.view(invoice_id_or_code)` - view created invoice(s).

*Usage*

```python
from paystackapi.invoice import Invoice
response = Invoice.view(
            invoice_id_or_code="PRQ_kp4lleqc7g8xckk",
        )
```

*Arguments*
- `invoice_id_or_code`: invoice ID or Code (string)

*Returns*

JSON data from Paystack API.

#### `Invoice.verify(invoice_code)` - verify created/existing invoice.

*Usage*

```python
from paystackapi.invoice import Invoice
response = Invoice.verify(
            invoice_code="PRQ_kp4lleqc7g8xckk",
        )
```

*Arguments*
- `invoice_code`: invoice Code (string)

*Returns*

JSON data from Paystack API.


#### `Invoice.send_notification(id_or_code)` - Send invoice notification.

*Usage*

```python
from paystackapi.invoice import Invoice
response = Invoice.send_notification(
            id_or_code="PRQ_kp4lleqc7g8xckk",
        )
```

*Arguments*
- `id_or_code`: id or code (string)

*Returns*

JSON data from Paystack API.


#### `Invoice.dashboard_metrics()` - Get dashboard metrics
*Usage*

```python
from paystackapi.invoice import Invoice
response = Invoice.dashboard_metrics()
```

*Arguments*
	No Arguments required

*Returns*
	JSON data from Paystack API.


#### `Invoice.finalize_draft(id_or_code, **kwargs)` - Finalize a draft
*Usage*

```python
from paystackapi.invoice import Invoice
response = Invoice.finalize_draft(
            id_or_code="PRQ_kp4lleqc7g8xckk",
            send_notification=False
        )
```

*Arguments*
- `id_or_code`: ID or Code (string)
- `send_notification`: Indicates whether Paystack sends an email notification to customer. Defaults to true. (Boolean)

*Returns*
	JSON data from Paystack API.


#### `Invoice.update(id_or_code, **kwargs)` - Update a draft
*Usage*

```python
from paystackapi.invoice import Invoice
response = Invoice.update(
            id_or_code="PRQ_kp4lleqc7g8xckk",
            amount=450000
        )
```

*Arguments*
- `id_or_code`: ID or Code
- `**kwargs`

*Returns*
	JSON data from Paystack API.


#### `Invoice.archive(id_or_code)` - Archive a draft
*Usage*

```python
from paystackapi.invoice import Invoice
response = Invoice.archive(
            id_or_code="PRQ_kp4lleqc7g8xckk",
        )
```

*Arguments*
- `id_or_code`: ID or Code

*Returns*
	JSON data from Paystack API.

#### `Invoice.update_transfer_recipient(recipient_code_or_id, **kwargs)` - Update transfer recipienta draft
*Usage*

```python
from paystackapi.invoice import Invoice
response = Invoice.update_transfer_recipient(
            recipient_code_or_id="PRQ_kp4lleqc7g8xckk",
            name="new name",
            email="new@email.com"
        )
```

*Arguments*
- `recipient_code_or_id`: recipient code or ID
- `name`: a name for the recipient (string)
- `email`: the email address of the recipient (string)

*Returns*
	JSON data from Paystack API.

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

- `type`: Recipient Type (Only nuban at this time)
- `name`: A name for the recipient
- `account_number`: Required if type is nuban
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

- `perPage`: records you want to retrieve per page (Integer)
- `page`: what page you want to retrieve (Integer)


*Returns*

JSON data from Paystack API.


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


Miscellaneous
-------------

``Misc.list_banks()`` - List Banks

```python
   from paystackapi.misc import Misc
   response = Misc.list_banks()
```
*Returns*

JSON data from paystack API.

