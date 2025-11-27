# Python Class Anatomy: The Ultimate Cheat Sheet 🐍✨

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![OOP](https://img.shields.io/badge/OOP-Fundamentals-brightgreen)
![Education](https://img.shields.io/badge/Perfect%20for-Learning-orange)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **A single, crystal-clear Python class that demonstrates *every* major class concept in one place.**  
> Perfect for beginners learning OOP, intermediates brushing up, or interviewers testing your depth.

```python
class ClassName:
    class_variable = "I belong to the class"

    def __init__(self, param1, param2):
        self.instance_var = param1    # belongs to each object

    def instance_method(self):
        return self.instance_var      # needs `self`

    @classmethod
    def class_method(cls):
        return cls.class_variable     # uses `cls`, accesses class state

    @staticmethod
    def static_method():
        return "No self or cls needed"  # just a namespaced function!

    @property
    def name(self):
        return self._name             # getter — use like an attribute

    @name.setter
    def name(self, value):
        self._name = value            # controlled mutation
```
# Why This Class Is Pure Gold
This isn't just code — it's a complete OOP reference packed into ~25 lines.

```
>>> obj = ClassName("Hello", 42)
>>> obj.instance_var
'Hello'

>>> obj.instance_method()
'Hello'

>>> ClassName.class_method()        # call on class
'I belong to the class'
>>> obj.class_method()              # or on instance!
'I belong to the class'

>>> ClassName.static_method()
'No self or cls needed'

>>> obj.name = "Grok"               # uses setter
>>> obj.name                        # uses getter
'Grok'
```
## Perfect For

Learning Python OOP from scratch
Teaching students the difference between self, cls, and no binding
Interview prep ("Explain @classmethod vs @staticmethod")
Keeping as a personal reference (you'll thank yourself later)

## Challenge Yourself!

```
# Can you add:
# 1. A class that counts how many instances were created?
# 2. A @property that returns the instance's memory address nicely?
# 3. A @classmethod that creates an instance from a string?
```

