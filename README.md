<div align="center">
  <img src="https://ditchcarbon.com/wp-content/uploads/2021/05/Group-119.svg"><br>
</div>

-----------------

# ditchcarbon-python

![PyPI](https://img.shields.io/pypi/v/ditchcarbon-python?color=5CB381)
![PyPI - Downloads](https://img.shields.io/pypi/dm/ditchcarbon-python?color=5CB381)
![PyPI - License](https://img.shields.io/pypi/l/ditchcarbon-python?color=5CB381)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ditchcarbon-python?color=5CB381)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ditchthis/ditchcarbon-python?color=5CB381)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## What is it?

**ditchcarbon-python** is the official Python wrapper for the DitchCarbon API. DitchCarbon calculates the carbon impact of almost anything using a combination of GHG protocol approved calculations and an unparalleled database of company and product disclosures.

## Where to get it?

You can install the library via PyPI (hosted [here](https://pypi.org/project/ditchcarbon-python)):

```sh
pip3 install ditchcarbon-python
```

The source code is currently hosted on GitHub, [here](https://github.com/ditchthis/ditchcarbon-python).

## How to use it?

First, import and initialise the library with your API token:

```python
from ditchcarbon_python import Client
ditchcarbon = Client(token="YOUR_TOKEN")
```

Then, use it:

```python
# Activities
ditchcarbon.activities.retrieve(1)
ditchcarbon.activities.retrieve_many(**params)
ditchcarbon.activities.retrieve_assessment(1, **params)
ditchcarbon.activities.retrieve_categories(**params)

# Categories
ditchcarbon.categories.search(**params)

# Expenses
ditchcarbon.expenses.calculate_emissions(**params)

# Products
ditchcarbon.products.calculate_emissions(**params)

# Servers
ditchcarbon.servers.find(**params)
ditchcarbon.servers.retrieve(1)
ditchcarbon.servers.calculate_emissions(1, **params)

# Suppliers
ditchcarbon.suppliers.calculate_emissions(**params)
```

## Documentation and Help
View our API reference [here](https://docs.ditchcarbon.com/reference). For usage questions, feel free to contact us [here](mailto:enquiries@ditchcarbon.com).
