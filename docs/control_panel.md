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
