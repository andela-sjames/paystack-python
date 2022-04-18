# paystack-python

[![Coverage Status](https://coveralls.io/repos/github/andela-sjames/paystack-python/badge.svg?branch=develop)](https://coveralls.io/github/andela-sjames/paystack-python?branch=master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/andela-sjames/paystack-python/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/andela-sjames/paystack-python/?branch=master)
[![Circle CI](https://img.shields.io/badge/license-MIT-blue.svg)](https://img.shields.io/badge/license-MIT-blue.svg) [![Build Status](https://travis-ci.org/andela-sjames/paystack-python.svg?branch=master)](https://travis-ci.org/andela-sjames/paystack-python)
[![PyPI version](https://badge.fury.io/py/paystackapi.svg)](https://badge.fury.io/py/paystackapi)

Python plugin for [Paystack](https://paystack.com/)
View on [pypi.python.org](https://pypi.python.org/pypi/paystackapi)

## Installation

```shell
pip install paystackapi
```

## Instantiate Paystack

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

### API Reference: [API](https://paystack.com/docs/api/)

### Other methods can be found in the docs folder

### Static Use

To start using the Paystack Python API, you need to start by setting your secret key.

You can set your secret key in your environment by running:

```bash
export PAYSTACK_SECRET_KEY = 'your_secret_key'
```

> Don't forget to get your API key from [Paystack](https://paystack.com/) and assign to the variable `PAYSTACK_SECRET_KEY`

### Available resources

```Python

BulkCharge
Charge
ControlPanel
Customer
Invoice
Misc
Page
Plan
Product
Refund
Settlement
SubAccount
Subscription
Transaction
TransferControl
Transfer
TransferSplit
TransferRecipient
Verification

```

Please reference the **[docs](https://github.com/andela-sjames/paystack-python/tree/master/docs)** folder for usage,
