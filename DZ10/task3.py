'''
Создать метакласс для паттерна Синглтон (см. конец вебинара)
'''


class MyMetaClass(type):
    a = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.a:
            cls.a[cls] = super(MyMetaClass, cls).__call__(*args, **kwargs)
        return cls.a[cls]


class MyClass(metaclass=MyMetaClass):
    pass


class TestClass():
    pass


a_obj = MyClass()
b_obj = MyClass()
print(a_obj == b_obj)

a_obj = TestClass()
b_obj = TestClass()
print(a_obj == b_obj)
