# Реализовать дескриптор валидации для атрибута email. Ваш дескриптор должен проверять формат email
# который вы пытаетесь назначить.

class EmailDescriptor:
    def __init__(self):
        pass
        # self.email
    def __get__(self, instance, owner):

            return self.email


    def __set__(self, instance, value):
        print(value.find('@'))
        if (('@' in value) and ('.' in value) and (0 < value.find('@') < (value.find('.') - 1))):
            print(value.find('@'))
            self.email = value
        else:
            raise Exception


class MyClass:
    email = EmailDescriptor()

my_class = MyClass()
my_class.email = "validemail@gmail.com"
print(my_class.email)

my_class.email = "novalidemail"
# Raised Exception