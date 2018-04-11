class Animal(object):
    def run(self):
        print('animal is runnuing')
    def run_twice(self):
        self.run()
        self.run()

class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):
    def run(self):
        print('cat is running...')
def run_3(animal):
    animal.run()
    animal.run()
    animal.run()

if __name__=='__main__':
    '''
    dog=Dog()
    # dog.run()
    dog.run_twice()
    cat = Cat()
    run_3(cat)
    cat.run_twice()
    # cat.run()
    print('')
   
    print(isinstance(cat,Animal))
    print(isinstance(cat, Dog))
    '''
    print(type(123))