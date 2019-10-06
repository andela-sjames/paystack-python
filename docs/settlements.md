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
