class Animal(object):
    def __init__(self,species,name,age):
      self.species=species
      self.name=name
      self.age=age
    def print_details(self):
      print("The Species is %s"%(self.species))
      print("The Name is %s"%(self.name))
      print("the age is %d"%(self.age))

## Dog is-a Animal
class Dog(Animal):

    def __init__(self,name):
        ## Dog has-a name
        self.name=name

## cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## cat has-a name
        self.name = name


## person is-a object
class Person(object):

    def __init__(self, name):
        ## person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has-a name
        super(Employee, self).__init__(name)
        ## Employee has a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salman is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a FIsh
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet satan 
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has a pet rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salman
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()


cow=Animal('mamal','cow',5)

print(cow.print_details())
