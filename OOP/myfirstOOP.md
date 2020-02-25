The code to the questions:
```.py
# This is the first practice for OOP

# get the biggest number
def get_biggest_number(*args):
    print(f'The biggest is {max(args)} years old')


# Exercise 1
class Dogs:
    # Class Attribute
    species = 'mammal'

    # Initializer
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the dog object
tom = Dogs("Tom", 3)
lily = Dogs("Lily", 9)
alison = Dogs("Alison", 12)

# The arguments we are passing
get_biggest_number(tom.age, lily.age, alison.age)
print(Dogs.species)

# Exercise 2, 3, 4

# Parent class
class Pets:
    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())

class Dog:
    # Class Attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old."

    # instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

    def is_hungry(self):
        return True

    def eat(self):
        self.is_hungry != self.is_hungry

    def walk(self):
        return f"{self.name} is walking!"

# Child class
class RusssellTerrier(Dog):
    def run(self, speed):
        return f"{self.name} runs {speed}"




# Instantiate the dog object
rikio = RusssellTerrier("Rikio", 12)
tuan = Dog("Tuan", 16)
ziyad = Dog("Ziyad", 90)

# Instances of dog
alldogs = [rikio, tuan, ziyad]

# Output
print(f"I have {len(alldogs)} dogs.")
for i in alldogs:
    i.eat()
    print(f" {i.name} is {i.age}")
    # problem: the last one does not work
print("And they're all {}s, of course.".format(Dog.species))

allpets = Pets(alldogs)

# IDK how to do this part really
for i in allpets.dogs:
    if Dog.is_hungry:
        print("My dogs are hungry")
    else:
        print("My dogs are not hungry")
        
# Exercise 4
allpets.walk()
```

Answers to the questions:
1. What is a class?

  Classes are used to create new user-defined data structures that contain arbitrary information about something. In the case of an animal, we could create an Animal() class to track properties about the Animal like the name and age.
  
1. What's an instance?

  An instance is a copy of the class with actual values, literally an object belonging to a specific class. It’s not a template anymore; it’s an actual animal, like a dog named Roger who’s eight years old.

1. What's the relationship between a class and an instance?

  a class is like a form or questionnaire. It defines the needed information. After you fill out the form, your specific copy is an instance of the class; it contains actual information relevant to you.

1. What's the Python syntax used for defining a new class?

  ```.py
  class()
  ```

1. What’s the spelling convention for a class name?

  CamelCase notation, starting with a capital letter

1. How do you instantiate, or create an instance of, a class?

   Use the __init__() method to initialize (e.g., specify) an object’s initial attributes by giving them their default value (or state). 

1. What’s a method?

  Instance methods or simply functions, are defined inside a class and are used to define the behaviours of the objects. They can also be used to perform operations with the attributes of our objects. Like the __init__ method, the first argument is always self:

1. What’s the purpose of self?

  This method must have at least one argument as well as the self variable, which refers to the object itself (e.g., Dog).

1. What’s the purpose of the __init__ method?

  Use the __init__() method to initialize (e.g., specify) an object’s initial attributes by giving them their default value (or state). 

1. Describe how inheritance helps prevent code duplication.

  If you have two classes that share many of the same methods AND share many of the same properties and fields then I would create a parent class. Inheritance is probably your best solution here.

1. Can child classes override properties of their parents?

  no
