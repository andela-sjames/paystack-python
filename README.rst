paystack-python
===============

|Coverage Status| |Scrutinizer Code Quality| |Circle CI| |Build Status|
|PyPI version|

| Python plugin for `Paystack <https://paystack.com/>`__
| View on `pypi.python.org <https://pypi.python.org/pypi/paystackapi>`__

Installation
============

::

    pip install paystackapi

Instantiate Paystack
====================

.. code:: python

    from paystackapi.paystack import Paystack
    paystack_secret_key = "5om3secretK3y"  
    paystack = Paystack(secret_key=paystack_secret_key)

    # to use transaction class  
    paystack.transaction.list()  

    # to use customer class  
    paystack.customer.get(transaction_id)

    # to use plan class  
    paystack.plan.get(plan_id)

Other methods can be found below...
'''''''''''''''''''''''''''''''''''

Static Use
==========

To start using the Paystack Python API, you need to start by setting
your secret key.

You can set your secret key in your environment by running:

.. code:: bash

    export PAYSTACK_SECRET_KEY = 'your_secret_key'

    Don't forget to get your API key from
    `Paystack <https://paystack.com/>`__ and assign to the variable
    ``PAYSTACK_SECRET_KEY``

Transactions
------------

``Transaction.initialize(reference, amount, email, plan)`` - Initialize transaction.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

*Usage*

.. code:: python

    from paystackapi.transaction import Transaction
    response = Transaction.initialize(reference='reference', 
                                      amount='amount', email='email')

*Arguments*

-  ``reference``: Unique transaction reference
-  ``amount``: Amount
-  ``email``: Email address
-  ``plan``: Specified plan (optional)

*Returns*

JSON data from Paystack API.

``Transaction.charge(reference, authorization_code, email, amount)`` - Charge authorization.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    from paystackapi.transaction import Transaction
    response = Transaction.charge(reference='reference', 
                                  authorization_code='authorization_code',
                                  email='email',
                                  amount='amount')

*Arguments*

-  ``reference``: Unique transaction reference
-  ``authorization_code``: Authorization code for the transaction
-  ``email``: Email Address of the user with the authorization code
-  ``amount``: Amount in kobo

*Returns*

JSON data from Paystack API.

``Transaction.charge_token(reference, token, email, amount)`` - Charge Token.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    from paystackapi.transaction import Transaction
    response = Transaction.charge_token(reference='reference',
                                        token='token', email='email',
                                        amount='amount')

*Arguments*

-  reference: unique transaction reference
-  token: paystack token
-  email: Email Address
-  amount: Amount in Kobo

*Returns*

JSON data from Paystack API.

``Transaction.get(transaction_id)`` - Get a single transaction.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    from paystackapi.transaction import Transaction
    response = Transaction.get(transaction_id=23)

*Arguments*

-  ``id``: Transaction id(integer).

*Returns*

JSON data from paystack API.

``Transaction.list()`` - List transactions.
'''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    from paystackapi.transaction import Transaction
    response = Transaction.list()

*Arguments*

No argument required.

*Returns*

JSON data from paystack API.

``Transaction.totals()`` - Get totals.
''''''''''''''''''''''''''''''''''''''

.. code:: python

    from paystackapi.transaction import Transaction
    response = Transaction.totals()

*Arguments*

No argument required.

*Returns*

JSON data from paystack API.

``Transaction.verify(reference)`` - Verify transactions.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    from paystackapi.transaction import Transaction
    response = Transaction.verify(reference='reference')

*Arguments*

-  ``reference``: a unique value needed for transaction.

*Returns*

JSON data from paystack API.

Plans
-----

``Plan.create(name, description, amount, interval, send_invoices, send_sms, hosted_page, hosted_page_url, hosted_page_summary, currency)`` - Create a plan
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    from paystackapi.plan import Plan  
    response = Plan.create(name='value', description='value', 
                           amount=amount, interval='value', 
                           send_invoices='value', 
                           send_sms='value',
                           hosted_page='value', 
                           hosted_page_url='value',
                           hosted_page_summary='value', 
                           currency='value')

*Arguments*

-  ``name``: plan's name.
-  ``description``: description of the plan.
-  ``amount``: amount for the plan in kobo
-  ``interval``: plan's interval(daily...etc)
-  ``send_invoices``: boolean
-  ``send_sms``: (optional)
-  ``hosted_page``: (optional)
-  ``hosted_page_url``: url of hosted page (optional)
-  ``hosted_page_summary``: summary of the hosted page
-  ``currency``: plans currency (NGN)

*Returns*

JSON data from paystack API.

``Plan.get(plan_id)`` - Get a single plan.
''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    from paystackapi.plan import Plan  
    response = Plan.get(plan_id=25)

*Arguments*

-  ``id``: paystack plan id.

*Returns*

JSON data from paystack API.

``Plan.list()`` - List paystack plan
''''''''''''''''''''''''''''''''''''

.. code:: python

    from paystackapi.plan import Plan  
    response = Plan.list()

*Arguments*

No argument required.

*Returns*

JSON data from paystack API.

``Plan.update(plan_id=88, name=None, description=None, amount=None, interval=None, send_invoices=None, send_sms=None, hosted_page=None, hosted_page_url=None, hosted_page_summary=None, currency=None)`` - Update paystack plan
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    from paystackapi.plan import Plan  
    response = Plan.update(plan_id=23, name=None, description=None,
                           amount=None, interval=None,
                           send_invoices=None, send_sms=None,
                           hosted_page=None, hosted_page_url=None,
                           hosted_page_summary=None, currency=None)

*Arguments*

-  ``plan_id``: plan identity number.
-  ``name``: name of plan
-  ``description``: plan description(optional)
-  ``amount``: plan amount in Kobo
-  ``interval``: plan interval9(monthly, yearly, quarterly...etc)
-  ``send_invoice``: (optional)
-  ``send_sms``: (optional)
-  ``hosted_page``: (optional)
-  ``hosted_page_url``: (optional)
-  ``hosted_page_summary``: (optional)
-  ``currency``: Naira in kobo(NGN)

*Returns*

JSON data from paystack API.

Customers
---------

``Customer.create(first_name, last_name, email, phone)`` - Create customer
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    from paystackapi.customer import Customer  
    response = Customer.create(first_name='first_name', 
                               last_name='last_name',
                               email='email', phone='phone')

*Arguments*

-  ``first_name``: customer's first name.
-  ``last_name``: customer's last name.
-  ``email``: customer's email address.
-  ``phone``: customer's phone number.

*Returns*

JSON data from paystack API.

``Customer.get(customer_id)`` - Get customers by id
'''''''''''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    from paystackapi.customer import Customer  
    response = Customer.get(customer_id=24)

*Arguments*

-  ``id``: paystack customer id

*Returns*

JSON data from paystack API.

``Customer.list()`` - List paystack customers
'''''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    from paystackapi.customer import Customer  
    response = Customer.list()

*Arguments*

No argument required.

*Returns*

JSON data from paystack API.

``Customer.update(customer_id, first_name=None, last_name=None, email=None, phone=None)`` - Update paystack customer data by id.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    from paystackapi.customer import Customer  
    response = Customer.update(customer_id=24, first_name=None, 
                               last_name=None, email=None, 
                               phone=None)

*Arguments* - ``customer_id``: paystack customer id. - ``first_name``:
customer's first name(optional). - ``last_name``: customer's last
name(optional). - ``email``: customer's email address(optional). -
``phone``: customer's phone number(optional).

*Returns*

JSON data from paystack API.

.. |Coverage Status| image:: https://coveralls.io/repos/github/andela-sjames/paystack-python/badge.svg?branch=develop
   :target: https://coveralls.io/github/andela-sjames/paystack-python?branch=master
.. |Scrutinizer Code Quality| image:: https://scrutinizer-ci.com/g/andela-sjames/paystack-python/badges/quality-score.png?b=master
   :target: https://scrutinizer-ci.com/g/andela-sjames/paystack-python/?branch=master
.. |Circle CI| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://img.shields.io/badge/license-MIT-blue.svg
.. |Build Status| image:: https://travis-ci.org/andela-sjames/paystack-python.svg?branch=master
   :target: https://travis-ci.org/andela-sjames/paystack-python
.. |PyPI version| image:: https://badge.fury.io/py/paystackapi.svg
   :target: https://badge.fury.io/py/paystackapi
