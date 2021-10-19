class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter("pepe", 30)
player2 = PlayerCharacter("paco", 30)

print(player1)  # <__main__.PlayerCharacter object at 0x0000013F23B921D0>
print(player1.name, player1.age)  # pepe 30

player1.run()  # run
print(player1.run())  # done

player2.attack = 40

print(player2.attack)  # 40
