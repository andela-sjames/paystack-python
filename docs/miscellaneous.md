
Miscellaneous
-------------

``Misc.list_banks()`` - List Banks

```python
   from paystackapi.misc import Misc
   response = Misc.list_banks()
```

Or with keyword args - the args are query params on the Paystack API.

```python
   from paystackapi.misc import Misc
   response = Misc.list_banks(country="ghana", currency="NGN")
```
*Optional Arguments*

- `country`: Country to return its banks
- `currency`: Currency 
- `gateway`: Gateway type of banks 

*Returns*

JSON data from paystack API.
