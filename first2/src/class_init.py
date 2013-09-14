class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sayHi(self):
        print('Hello, my name is', self.name, 'and i am', self.age, 'years old')

p = Person('Christian', 23)
p.sayHi()

# This short example can also be written as Person('Swaroop').sayHi() #