class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'pepe',
            'has_pets': False
        }

    def __len__(self):
        return 5

    def __del__(self):
        print('deleted!')

    def __call__(self):
        return('yes??')

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)

print(action_figure.__str__())  # <__main__.Toy object at 0x000001F10F677CA0>
print(str(action_figure))  # <__main__.Toy object at 0x000001F10F677CA0>

print(len(action_figure))  # 5

# del action_figure  # deleted!

print(action_figure())  # yes??

print(action_figure['name'])  # pepe
