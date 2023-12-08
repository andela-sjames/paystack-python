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
- `invoice_id_or_code`: invoice ID or code (string)

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
