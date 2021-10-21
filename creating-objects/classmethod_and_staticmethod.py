class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @classmethod
    def adding_things_2(cls, num1, num2):
        return cls("paco", num1 + num2)

    @staticmethod
    def adding_things_3(num1, num2):
        return num1 + num2


print(PlayerCharacter.adding_things(2, 2))  # 4

player2 = PlayerCharacter.adding_things_2(20, 15)

print(player2.age)  # 35

player1 = PlayerCharacter("pepe", 30)

print(player1.adding_things(2, 2))  # 4

print(player2.adding_things_3(10, 10))  # 20

print(PlayerCharacter.adding_things_3(10, 10))  # 20
