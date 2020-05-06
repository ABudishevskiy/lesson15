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
             print(owner)
             print(self.method)
             if issubclass(owner, N):
                 return self.method(owner)
             return owner.__name__ + "aaa"
         return nnew_func

class C:
    @myClassMethod
    def nfunc(cls, *args):
        print(cls.__name__)

        return 13

class N(C):
    pass
class D(C):
    pass
k = N()
l = D()
print(k.nfunc())
print(l.nfunc())
print(N.nfunc())
print(D.nfunc())