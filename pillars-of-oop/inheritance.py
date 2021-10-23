class User(object):  # when creating a class, automatically inherits from object
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attack with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'attack with {self.arrows} arrows')


wizard1 = Wizard('pepe', 20)
archer1 = Archer('paco', 100)

wizard1.sign_in()

wizard1.attack()

archer1.attack()


# True:
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))

# everything in python inherits from the base object class. so everything is an object:
print(isinstance(wizard1, object))  # True
