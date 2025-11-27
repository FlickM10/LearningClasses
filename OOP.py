class ClassName:
    class_variable = "I belong to the class"

    def __init__(self, param1, param2):
        self.instance_var = param1      # instance variable

    def instance_method(self):
        return self.instance_var

    @classmethod
    def class_method(cls):
        return cls.class_variable

    @staticmethod
    def static_method():
        return "No self or cls needed"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
