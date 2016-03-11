Installation
============

``pip install paystack-python-library``

Usage
=====

::

    from paystack.constants import PAYSTACK_SECRET_KEY
    PAYSTACK_SECRET_KEY = 'your_secret_key`

Transactions
------------

Create a plan
^^^^^^^^^^^^^

::

    from paystack.transaction import Transaction
    response = Transaction.create(name, description, amount, interval,
                                  send_invoices, send_sms,
                                  hosted_page, hosted_page_url,
                                  hosted_page_summary, currency)
        Args:
            name: plan's name.
            description: description of the plan.
            amount: amount for the plan in kobo
            interval: plan's interval(daily...etc)
            send_invoices: boolean
            send_sms: (optional)
            hosted_page: (optional)
            hosted_page_url: url of hosted page (optional)
            hosted_page_summary: summary of the hosted page
            currency: plans currency (NGN)

        Returns:
            Json data from paystack API.

Get a single plan.
^^^^^^^^^^^^^^^^^^

::

    from paystack.transaction import Transaction
    response = Transaction.get(id)

        Args:
            id: paystack plan id.
        Returns:
            Json data from paystack API.

List paystack plan
^^^^^^^^^^^^^^^^^^

::

    from paystack.transaction import Transaction
    response = Transaction.list()

        Args:
            No argument required.
        Returns:
            Json data from paystack API.

Update paystack plan
^^^^^^^^^^^^^^^^^^^^

::

    from paystack.transaction import Transaction
    response = Transaction.update(id, name=None, description=None,
                                  amount=None, interval=None,
                                  send_invoices=None, send_sms=None,
                                  hosted_page=None, hosted_page_url=None,
                                  hosted_page_summary=None, currency=None)

        Args:
            id: plan identity number.
            name: name of plan
            description: plan description(optional)
            amount: plan amount in Naira
            interval: plan interval9(monthly, yearly, quarterly...etc)
            send_invoice: (optional)
            send_sms: (optional)
            hosted_page: (optional)
            hosted_page_url: (optional)
            hosted_page_summary: (optional)
            currency: Naira in kobo(NGN)
        Returns:
            Json data from paystack API.

Customers
---------

--------------

Create customer
^^^^^^^^^^^^^^^

::

    from paystack.transaction import Transaction
    response = Transaction.create(first_name, last_name, email, phone)

        Args:
            first_name: customer's first name.
            last_name: customer's last name.
            email: customer's email address.
            phone:customer's phone number.

        Returns:
            Json data from paystack API.

Get customers by id
^^^^^^^^^^^^^^^^^^^

::

    from paystack.transaction import Transaction
    response = Transaction.get(id)

        Args:
            id: paystack customer id.
        Returns:
            Json data from paystack API.

List paystack customers
^^^^^^^^^^^^^^^^^^^^^^^

::

    from paystack.transaction import Transaction
    response = Transaction.list()

        Args:
            No argument required.
        Returns:
            Json data from paystack API.

Update paystack customer data by id.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    from paystack.transaction import Transaction
    response = Transaction.update(id, first_name=None,
                                  last_name=None,
                                  email=None, phone=None)

        Args:
            id: paystack customer id.
            first_name: customer's first name(optional).
            last_name: customer's last name(optional).
            email: customer's email address(optional).
            phone:customer's phone number(optional).

        Returns:
            Json data from paystack API.
