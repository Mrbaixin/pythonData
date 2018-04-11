class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# *************活动
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')
# 各种动物:
class Dog(Mammal,Runnable):
    pass

class Bat(Mammal,Runnable):
    pass

class Parrot(Bird,Flyable):
    pass

class Ostrich(Bird,Flyable):
    pass

d=Dog()
d.run()
# ******************************************https://kevinguo.me/2018/01/19/python-topological-sorting/
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class A(object):
    def foo(self):
        print('A foo')
    def bar(self):
        print('A bar')

class B(object):
    def foo(self):
        print('B foo')
    def bar(self):
        print('B bar')

class C1(A,B):
    pass

class C2(A,B):
    def bar(self):
        print('C2-bar')

class D(C1,C2):
    pass

if __name__ == '__main__':
    print(D.__mro__)
    d=D()
    d.foo()
    d.bar()


class A(object):
        def foo(self):
            print('A foo')

        def bar(self):
            print('A bar')


class B(object):
        def foo(self):
            print('B foo')

        def bar(self):
            print('B bar')


class C1(A):
        pass


class C2(B):
        def bar(self):
            print('C2-bar')


class D(C1, C2):
        pass


if __name__ == '__main__':
        print(D.__mro__)
        d = D()
        d.foo()
        d.bar()