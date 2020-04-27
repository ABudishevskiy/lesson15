# Создать свой тип с помощью type
def metod(self, value):
    return value/6

def my_class_init(self, attr_value):
     self.my_attribute = attr_value

MyClass = type('MyClass', (object,), {'__init__': my_class_init, 'met': metod})
o = MyClass(7)
print(o.my_attribute)
print(o.met(6))

MynClass = type('MyClass', (object,), {'met': metod})
p = MynClass()
print(o.met(6))
