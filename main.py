from datetime import date

class Monster:

    color = "black" #class attributes

    def __init__(self, age, name): #constructor
        #instace attributes
        self.age = age
        self.name = name

        self._is_innocent = None #private attribute by convention

    #instance method
    def steal(self, warrior):
        warrior.lose_stick()
        #self._number_of_sticks += 1

    #def change_warrior_age(self, warrior):
        #new_age = 5
        #warrior.age = new_age

    @classmethod
    def create_monster_from_birth_year(cls, year, name):
        return cls(date.today().year - year, name)

    @staticmethod
    def is_adult_monster(age):
        return age > 18

# creating an instance
monster1 = Monster(15,"mon1")

# accessing attributes
print("mon1 default age :-", monster1.age)

# changing attribute value
monster1.age = 10
print("mon1 updated age :-", monster1.age)

# creating another instance
monster2 = Monster(10,"mon2")
print("mon2 age :-", monster2.age)

#mon color
print("mon1 color :-", monster1.color)
print("mon2 color :-", monster2.color)
