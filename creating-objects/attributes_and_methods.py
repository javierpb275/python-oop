class PlayerCharacter:
    # class object attribute (static attribute)
    membership = True

    def __init__(self, name, age):
        if (PlayerCharacter.membership):  # here we access a property of the class (not the object)
            self.name = name
            self.age = age

    def sayMyName(self):
        print(f'my name is {self.name}')  # self: refers to the object created

    def saySth(self, sth):
        print(f'{sth}')


player1 = PlayerCharacter("pepe", 30)
player2 = PlayerCharacter("paco", 30)

print(player1.membership)  # True
print(player2.membership)  # True

player1.sayMyName()  # my name is pepe
player2.saySth("hello")  # hello


# help gives us information about the object like the class, the attributes, the methods...
# help(player1)
