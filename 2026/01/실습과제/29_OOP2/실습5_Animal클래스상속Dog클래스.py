# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0
    def __init__(self):
        self.increase_animal()
        

    @classmethod
    def increase_animal(cls):
        Animal.num_of_animal += 1
        return

class Dog(Animal):

    def bark(self):
        print("멍멍!")


dog1 = Dog()
dog1.bark()
