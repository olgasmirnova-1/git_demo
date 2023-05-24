class Dog:
    biology_class = 'Animal' #статический атрибут

    def __init__(self, name, weight, color):
        self.__name = name #динамический атрибут
        self.weight = weight
        self.color = color


    def run(self):
        return 'I can run!'

    def get_name(self):
        return f'Hello! My name is {self.__name}'

    def set_name(self, new_name):
        self.__name = new_name

dog1 = Dog('Mattly', 10, 'grey')

dog2 = Dog('Rubby', 5, 'black')
print(dog2._Dog__name)
print(dog2.get_name())
print(dog2.__dict__)
print(dog2.set_name('Terry'))
print(dog2.get_name())
# print(dog1.name)
# print(dog1.get_name())
# print(dog1.color)
# print(dog1.biology_class)
# #
# print(dog2.get_name())
# print(dog2.__dict__)
# dog2.name = 'Snoopy'
# print(dog2.get_name())
# print(dog2.biology_class)

class Pitbull(Dog):
    def __init__(self, name, weight, color, passport):
        super().__init__(name, weight, color)
        self.passport = passport

    def give_a_paw(self):
        return f"I can give a paw, because I'm {dog3.name}!"
    def run(self):
        return 'I can run fast!'

dog3 = Pitbull('Ground Honey', 15, 'black', 'type1')

# print(dog3.give_a_paw())
# print(dog3.get_name())
# print(dog2.run())
# print(dog3.run())

