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
