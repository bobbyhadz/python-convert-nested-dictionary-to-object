# Convert a nested dictionary to an Object in Python

class Struct:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, dict):
                self.__dict__[key] = Struct(**value)
            else:
                self.__dict__[key] = value


my_dict = {
    'name': 'bobbyhadz',
    'address': {
        'country': 'Country A',
        'city': 'City A',
        'codes': [1, 2, 3]
    },
}

obj = Struct(**my_dict)

print(obj.address.country)  # 👉️ Country A
print(obj.address.codes)  # 👉️ [1, 2, 3]
print(obj.name)  # 👉️ bobbyhadz

obj.address.greet = 'hello world'
print(obj.address.greet)  # 👉️ hello world