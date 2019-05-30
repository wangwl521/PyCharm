class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running')


def run_twice(animal):
    animal.run()
    animal.run()


a = Animal()
d = Dog()
c = Cat()

print('a is animal?', isinstance(a, Animal))
print('b is animal?', isinstance(a, Dog))
print('c is animal?', isinstance(a, Cat))

print('d is animal?', isinstance(d, Animal))
print('d is animal?', isinstance(d, Dog))
print('c is animal?', isinstance(d, Cat))

run_twice(c)
