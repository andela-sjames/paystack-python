Product
-------
#### `Product.create(**kwargs)` - Create a product

*Usage*

```python
from paystackapi.product import Product
response = Product.create(name="Product PyPaystack test",
						  description="Description of the product",
                          price=500000, currency="NGN", **kwargs)
```

*Arguments*

- `name`: Name of the product
- `description`: Description of product
- `price`: Price of the product, in kobo(Integer)
- `currency`: Currency in which the amount should be charged
- **kwargs

*Returns*

JSON data from Paystack API.


#### `Product.list()` - List created products

*Usage*

```python
from paystackapi.product import Product
response = Product.list()
```

*Arguments*

No argument required.

*Returns*

JSON data from Paystack API.


#### `Product.fetch(product_id)` - Fetch created Products by ID

*Usage*

```python
from paystackapi.product import Product
response = Product.fetch(product_id=5499)
```

*Arguments*

- `product_id`: Product ID (integer).

*Returns*

JSON data from Paystack API.


#### `Product.update(product_id, **kwargs)` - Update a created product by ID

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
- `currency`: Currency in which the amount should be charged
- `**kwargs`

*Returns*

JSON data from Paystack API.
