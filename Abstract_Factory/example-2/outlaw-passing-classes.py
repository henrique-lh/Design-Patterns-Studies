"""Now, python classes can't be passed as a value"""

import json
from decimal import Decimal

text = '{"total": 9.61, "items": ["Americano", "Omelet"]}'

# In Python: a factory function

def build_decimal(string):
    return Decimal(string.lstrip('$'))

# In some legacy languages: code must move inside a class method instead

class DecimalFactory(object):

    @staticmethod
    def build(string):
        return Decimal(string.lstrip('$'))

class Loader(object):

    @staticmethod
    def load(string, factory):
        string = string.rstrip(',') # allow trailing comma
        return [factory.build(item) for item in string.split(',')]

f = DecimalFactory()
result = Loader.load('464.80, 993.68', f)
print(result)