"""
As its name proclaims, SimpleNamespace is simple!
It’s basically a dictionary
that allows attribute access and prints nicely.
 Attributes can be added, modified, and deleted freely
"""

from types import SimpleNamespace

car3 = SimpleNamespace(
    color='brown',
    mileage=54567.12,
    automatic=True
)

car3.model = 'Toyota'

print(car3)  # namespace(color='brown', mileage=54567.12, automatic=True, model='Toyota')
