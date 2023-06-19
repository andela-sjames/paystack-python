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
response = SubAccount.fetch(id_or_slug="some_slug_like_subaccount_code_or_id")
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
            id_or_slug="some_slug_like_subaccount_code_or_id",
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
