Payment Page
-------
#### `Page.create(name, **kwargs)` - Create a Page

*Usage*

```python
from paystackapi.page import Page
response = Page.create(
            name="New test product One"
        )
```

*Arguments*
- `name`: name of page
- `**kwargs`

*Returns*

JSON data from Paystack API.

#### `Page.list(perPage, page)` - List a Page

*Usage*

```python
from paystackapi.page import Page
response = Page.list(perPage=3, page=1)
```

*Arguments*
- `perPage`: records you want to retrieve per page (Integer)
- `page`: what page you want to retrieve (Integer)

*Returns*

JSON data from Paystack API.

#### `Page.fetch(id_or_slug)` - Fetch a Page

*Usage*

```python
from paystackapi.page import Page
response = Page.fetch(id_or_slug="5nApBwZkvY")
```

*Arguments*
- `id_or_slug`: id or slug

*Returns*

JSON data from Paystack API.

#### `Page.update(id_or_slug)` - Update a Page by id_or_slug

*Usage*

```python
from paystackapi.page import Page
response = Page.update(id_or_slug="5nApBwZkvY", **kwargs)
```

*Arguments*
- `id_or_slug`: id or slug
- `**kwargs`

*Returns*

JSON data from Paystack API.

#### `Page.is_slug_available(id_or_slug)` - Check Slug Availability

*Usage*

```python
from paystackapi.page import Page
response = Page.is_slug_available(slug="new_or_existing_slug")
```

*Arguments*
- `slug`: URL slug to be confirmed

*Returns*

JSON data from Paystack API.

#### `Page.add_products(id_or_slug)` - Add products to payment page

*Usage*

```python
from paystackapi.page import Page
response = Page.add_products(
				payment_page_id="new_or_existing_slug"
            	product=[123, 456, 457]
            )
```

*Arguments*

- `payment_page_id`: Id of the payment page (Integer)
- `product`: Ids of all the products i.e. [473, 292]

*Returns*

JSON data from Paystack API.
