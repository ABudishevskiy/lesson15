# Реализовать классы дескрипторы StaticMethod и ClassMethod.


class mystaticmethod(object):
    def __init__(self, function):
        self.function = function

    def newfunc(self, *args, **kwargs):
        print('bye')
        print(*args)
        print(self.function(*args))



    def __get__(self, instance, owner):
        print(instance, owner)
        return self.newfunc

class A:
    @mystaticmethod
    def func(*args):
        print('hello', *args)
b = A()
print(b.func(5, 6))
print(A.func(3))


class myClassMethod(object):
     def __init__(self, method):
         self.method = method
     def __get__(self, instance, owner):
         if owner is None:
             owner = type(instance)
         def nnew_func(*args):
             if owner == N:
                     print('aaa')
                     self.method(owner)
                     return self.method
             print('bbb')
             self.method(owner)
             return self.method
         return nnew_func

class C:
    @myClassMethod
    def nfunc(cls, *args):
        if cls == N:
            print('hello aaa')
        if cls == D:
            print('hello bbb')
        return 13

class N(C):
    pass
class D(C):
    pass
k = N()
l = D()
print(k.nfunc())
print(k.nfunc(D))
print(l.nfunc())