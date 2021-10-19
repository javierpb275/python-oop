# OOP (Object Oriented Programming)
print(type(None))  # <class 'NoneType'>
print(type(True))  # <class 'bool'>
print(type(5))  # <class 'int'>
print(type(5.5))  # <class 'float'>
print(type('hi'))  # <class 'str'>
print(type([]))  # <class 'list'>
print(type(()))  # <class 'tuple'>
print(type({}))  # <class 'dict'>

'''
<class 'NoneType'>
<class 'bool'> 
<class 'int'>  
<class 'float'>
<class 'str'>
<class 'list'>
<class 'tuple'>
<class 'dict'>
'''

# creating a class:


class BigObject:
    pass


# create a new object by instanciating class BigObject:
obj1 = BigObject()
obj2 = BigObject()

print(type(obj1))  # <class '__main__.BigObject'>
