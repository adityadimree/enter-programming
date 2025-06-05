class my_class:
    def __init__(self):
        self._my_attribute = None
    @property
    def my_attribute(self):
        return self._my_attribute
    @my_attribute.setter
    def my_attribute(self, value):
        self._my_attribute = value
my_object = my_class()
my_object.my_attribute = 42
print(my_class.my_attribute)


