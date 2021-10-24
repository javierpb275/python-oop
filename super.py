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
