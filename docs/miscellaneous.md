
Miscellaneous
-------------

``Misc.list_banks()`` - List Banks

```python
   from paystackapi.misc import Misc
   response = Misc.list_banks()
```

Or with keyword args - the args are query params on Paystack.

```python
   from paystackapi.misc import Misc
   response = Misc.list_banks(country="ghana", currency="NGN")
```
*Returns*

JSON data from paystack API.
