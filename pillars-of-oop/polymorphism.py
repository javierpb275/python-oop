class User():
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attack with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'attack with {self.arrows} arrows')


wizard1 = Wizard('pepe', 20)
archer1 = Archer('paco', 40)


def player_attack(char):
    char.attack()


player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()

# polymorphism: it allows us to have many forms. it is the ability to redefine methods
# of derived classes like wizard and archer.
# an object that gets instatiated can behave in different forms based on polymorphism
