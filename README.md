# DitchCarbon Python Wrapper

Use this library to interact with the DitchCarbon API.

```python
from ditchcarbon_python import Client
client = Client(token="YOUR_TOKEN")

client.products.calculate_emissions(manufacturer="Apple", name="iPhone 12", price=1000)
```
View our API reference [here](https://docs.ditchcarbon.com/reference).
