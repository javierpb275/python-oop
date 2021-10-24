class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attack with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows, email):
        super().__init__(email)
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'attack with {self.arrows} arrows')


wizard1 = Wizard('pepe', 20, 'pepe@gmail.com')
archer1 = Archer('paco', 40, 'paco@gmail.com')

print(wizard1.email)
print(archer1.email)

# introspection: ability to determine the type of an object at runtime
print(dir(wizard1))  # list out the available methods of wizard1

""" 
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
    '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attack', 'email', 'name', 'power', 'sign_in']
 """
