Product
-------
#### `Product.create(**kwargs)` - Create a Product

*Usage*

```python
from paystackapi.product import Product
response = Product.create(name="Product pypaystack test",
						  description="my test description",
                          price=500000, currency="NGN", **kwargs)
```

*Arguments*

- `name`: Name of the product
- `description`: Description of product
- `price`: Price of the product, in kobo(Integer)
- `currency`: Currency in which amount should be charged
- **kwargs

*Returns*

JSON data from Paystack API.


#### `Product.list()` - list created Products

*Usage*

```python
from paystackapi.product import Product
response = Product.list()
```

*Arguments*

No argument required.

*Returns*

JSON data from Paystack API.


#### `Product.fetch(product_id)` - fetch created Products by id

*Usage*

```python
from paystackapi.product import Product
response = Product.fetch(product_id=5499)
```

*Arguments*

- `product_id`: Product id(integer).

*Returns*

JSON data from Paystack API.


#### `Product.update(product_id, **kwargs)` - update a created Product by id

*Usage*

```python
from paystackapi.product import Product
response = Product.update(product_id=5499, **kwargs)
```

*Arguments*

- `product_id`: Paystack product id.
- `name`: Name of the product
- `description`: Description of product
- `price`: Price of the product, in kobo(Integer)
- `currency`: Currency in which amount should be charged
- `**kwargs`

*Returns*

JSON data from Paystack API.
