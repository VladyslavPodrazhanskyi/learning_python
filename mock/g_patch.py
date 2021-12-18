"""
unittest.mock provides a powerful mechanism
for mocking objects, called patch(),
which looks up an object in a given module
and replaces that object with a Mock

use patch() as a decorator or a context manager
to provide a scope in which you will mock the target object.
"""

# 1. patch() as a decorator
# to mock an object for the duration of your entire test function
