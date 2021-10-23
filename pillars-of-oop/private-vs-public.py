class PlayerCharacter:
    def __init__(self, name, age):
        # to indicate that some atribute or method is private we put _ at the beginning
        # _ means that shouldn't touch this. please don't touch this.
        self._name = name
        self._age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter("pepe", 30)

player1._name = 'paco'

print(player1._name)  # paco: we can still change it but we shouldn't do it


# __init__ : is a Dunder Method. It is built into python
